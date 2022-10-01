from django.conf import settings
import hashlib

from butterfly.orders.models import Order


def generate_order_data(order: Order) -> dict[str, str]:
    """Generates order data for cloudipsp (Fondy)

    Args:
        order (Order): Order for generating data

    Returns:
        dict: order data
    """
    data = {
        "order_id": str(order.unique_id),
        "order_desc": generate_order_desc(order),
        "currency": "RUB",
        "amount": str(int(order.get_amount() * 100)),
    }
    signature = generate_signature(params=data)
    data = {**data, "signature": signature}

    return data


def generate_signature(params: dict[str, str]) -> str:
    """Generates signature for fondy. See https://docs.fondy.eu/ru/docs/page/3/#chapter-3-5

    Args:
        params (dict[str, str]): Parameters for signature generating

    Returns:
        str: Signature
    """
    params["merchant_id"] = str(settings.FONDY_MERCHANT_ID)

    sorted_params = sorted(params.items(), key=lambda p: p[0])
    values = map(lambda p: p[1], sorted_params)
    filtered_values = filter(lambda p: p, values)

    raw_signature = "|".join([settings.FONDY_SECRET_KEY] + list(filtered_values))
    signature = hashlib.sha1(raw_signature.encode("utf-8")).hexdigest()

    return signature


def generate_order_desc(order: Order) -> str:
    """Generates order description for Fondy

    Args:
        order (Order): Order for description generating

    Returns:
        str: Description
    """
    count = order.items.count()
    if count == 1:
        return order.items.all()[0].product.name
    elif count == 2:
        return ", ".join([i.product.name for i in order.items.all()])
    else:
        return f"{count} products"
