from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpRequest, JsonResponse
from django.contrib.auth.decorators import login_required

from butterfly.products.models import Product
from butterfly.cart.models import CartItem


@login_required
def add_product(request: HttpRequest):
    if request.method == "POST" and request.is_ajax():
        product_id = request.POST.get("product_id", "")
        print("first")
        if not product_id.isdigit():
            raise Http404()

        print("second")
        product = get_object_or_404(Product, pk=product_id)

        user = request.user
        if not user.favourites.filter(id=product_id):
            user.favourites.add(product)

        CartItem.objects.filter(product=product, cart=user.cart).delete()

        return JsonResponse(
            {
                "product": {"name": product.name},
                "total_price": user.cart.get_total_price(),
            }
        )

    raise Http404()


def index(request: HttpRequest):
    favourites = request.user.favourites.all()
    context = {
        "favourites": favourites,
    }
    return render(request, "favourites/favourites.html", context=context)
