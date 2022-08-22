from django.http import HttpResponseNotFound, JsonResponse
from django.shortcuts import get_object_or_404

from products.models import Product
from butterfly.cart.models import Cart, CartItem


def add_product(request):
    if request.method == 'POST' and request.is_ajax():
        product_id = request.POST.get('product_id', '')
        if not product_id or not product_id.isdigit():
            return HttpResponseNotFound()

        product = get_object_or_404(Product, pk=product_id)

        if not request.session or not request.session.session_key:
            request.session.save()

        if request.user.is_authenticated:
            cart, _ = Cart.objects.update_or_create(
                user=request.user,
                defaults={'session_key': request.session.session_key}
            )

        else:
            cart, _ = Cart.objects.get_or_create(
                session_key=request.session.session_key,
                defaults={'user': None}
            )

        cart_item, cart_item_created = CartItem.objects.get_or_create(
            cart=cart, product=product
        )

        cart.save()
        cart_item.save()

        return JsonResponse({'count': cart.items.count()})

    return HttpResponseNotFound()
