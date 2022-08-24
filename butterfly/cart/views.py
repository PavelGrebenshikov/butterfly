from django.http import HttpResponseNotFound, JsonResponse
from django.shortcuts import get_object_or_404

from products.models import Product
from butterfly.cart.models import Cart, CartItem


def add_product(request):
    if request.method == 'POST' and request.is_ajax():
        product_id = request.POST.get('product_id', '')
        product = get_object_or_404(Product, pk=product_id)

        if not request.session or not request.session.session_key:
            request.session.save()

        if request.user.is_authenticated:
            cart, _ = Cart.objects.get_or_create(user=request.user)

        else:
            try:
                cart = Cart.objects.get(
                    pk=request.session.get('cart_id')
                )

            except Cart.DoesNotExist:
                cart = Cart(user=None)

        cart.save()
        cart_item, _ = CartItem.objects.get_or_create(
            cart=cart, product=product
        )

        cart_item.save()

        request.session['cart_id'] = cart.id

        return JsonResponse({'count': cart.items.count()})

    return HttpResponseNotFound()
