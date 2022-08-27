from django.http import HttpResponseNotFound, JsonResponse
from django.shortcuts import get_object_or_404

from products.models import Product
from butterfly.cart.models import Cart, CartItem


def add_product(request):
    if request.method == 'POST' and request.is_ajax():
        product_id = request.POST.get('product_id')
        product = get_object_or_404(Product, pk=product_id)

        cart = Cart.get_cart(request)
        cart.save()

        cart_item, _ = CartItem.objects.get_or_create(
            cart=cart, product=product
        )
        cart_item.save()

        request.session['cart_id'] = cart.id
        return JsonResponse({'count': cart.items.count()})

    return HttpResponseNotFound()
