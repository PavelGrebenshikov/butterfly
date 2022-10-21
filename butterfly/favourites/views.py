from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, JsonResponse
from django.shortcuts import get_object_or_404, render

from butterfly.cart.models import Cart, CartItem
from butterfly.exceptions import HttpErrorException
from butterfly.products.models import Product


@login_required
def add_product(request: HttpRequest):
    if request.method == "POST" and request.is_ajax():
        product_id = request.POST.get("product_id", "")
        if not product_id.isdigit():
            raise HttpErrorException(400)

        product = get_object_or_404(Product, pk=product_id)

        user = request.user
        if not user.favourites.filter(id=product_id):
            user.favourites.add(product)

        cart = Cart.get_cart(request)
        CartItem.objects.filter(product=product, cart=cart).delete()

        return JsonResponse(
            {
                "product": {"name": product.name},
                "cart_total_price": cart.get_total_price(),
            }
        )

    raise HttpErrorException(405)


def index(request: HttpRequest):
    favourites = request.user.favourites.all()
    context = {
        "favourites": favourites,
    }
    return render(request, "favourites/favourites.html", context=context)
