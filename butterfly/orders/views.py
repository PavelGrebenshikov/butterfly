from cloudipsp import Api, Checkout
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import redirect

from butterfly.cart.models import Cart
from butterfly.orders.models import Order
from .payment import generate_order_data


@login_required
def create(request):
    if request.method == "POST":
        cart = Cart.get_cart(request)
        if not cart.items.count():
            raise Http404()

        order = Order(user=request.user)
        order.save()
        for i in cart.items.all():
            order.items.create(product=i.product, count=i.count)

        cart.items.all().delete()

        api = Api(
            merchant_id=settings.FONDY_MERCHANT_ID,
            secret_key=settings.FONDY_SECRET_KEY,
        )
        checkout = Checkout(api=api)

        data = generate_order_data(order)
        url = checkout.url(data).get("checkout_url")
        return redirect(url)

    raise Http404()
