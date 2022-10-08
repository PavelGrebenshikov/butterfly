import hashlib

import pytest
from django.conf import settings
from django.test import RequestFactory

from butterfly.orders.models import Order
from butterfly.orders.payment import (
    generate_order_desc,
    generate_signature,
    get_cleaned_request_data,
)

pytestmark = pytest.mark.django_db


@pytest.mark.parametrize(
    "order, expected",
    [
        ("single product", "First"),
        ("two products", "First, Second"),
        ("many products", "3 products"),
    ],
)
def test_generate_order_desc(
    created_orders: dict[str, Order], order: str, expected: str
):
    assert generate_order_desc(created_orders[order]) == expected


def test_get_cleaned_request_data():
    rf = RequestFactory()

    rf.POST = {
        "some": "data",
        "signature": "blablabla",
        "response_signature_string": "blablabla",
    }

    assert get_cleaned_request_data(rf) == {"some": "data"}


def test_generate_signature():
    signature = hashlib.sha1(
        f"{settings.FONDY_SECRET_KEY}|{settings.FONDY_MERCHANT_ID}|data".encode("utf-8")
    ).hexdigest()
    assert generate_signature({"some": "data"}) == signature
