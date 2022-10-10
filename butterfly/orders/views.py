import uuid

from cloudipsp import Api, Checkout
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from butterfly.cart.models import Cart
from butterfly.orders.models import Order

from .payment import check_signature, generate_order_data


@login_required
def index(request):
    orders = request.user.orders.order_by("-created_at")
    context = {"orders": orders}
    return render(request, "orders/orders.html", context=context)


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
        cart.delete()

        api = Api(
            merchant_id=settings.FONDY_MERCHANT_ID,
            secret_key=settings.FONDY_SECRET_KEY,
        )
        checkout = Checkout(api=api)

        data = generate_order_data(order, request)
        url = checkout.url(data).get("checkout_url")
        return redirect(url)

    raise Http404()


@csrf_exempt
def approve_payment(request):
    if request.method == "POST":
        payment_data = request.POST
        order = get_object_or_404(Order, unique_id=payment_data.get("order_id"))
        if check_signature(request):
            order.status = payment_data["order_status"]
            order.save()
            return redirect(reverse("users:redirect"))

        raise Http404()

    raise Http404()
