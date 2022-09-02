from django.http import JsonResponse, Http404, HttpResponse
from django.shortcuts import get_object_or_404, render

from products.models import Product
from butterfly.cart.models import Cart, CartItem


def index(request):
    cart = Cart.get_cart(request)
    context = {
        'cart_items': cart.items.all(),
        'total_price': cart.get_total_price(),
        'user': request.user
    }
    return render(request, 'cart/index.html', context=context)


def add_product(request):
    """Adds product to cart (ajax)

    POST args:
        product_id (int): Product pk
    Returns:
        HttpResponse | Http404

    """
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
        return HttpResponse()

    return Http404()


def change_item_count(request):
    """Increments or decrements cart item.count value (ajax)

    POST args:
        product_id (int): Product pk
        sign ('+' or '-'): Increment (+) or decrement (-) value
    Returns:
        JsonResponse | Http404

    """
    if request.method == 'POST' and request.is_ajax():
        product_id = request.POST.get('product_id')
        product = get_object_or_404(Product, pk=product_id)

        cart = Cart.get_cart(request)
        item = get_object_or_404(cart.items, product=product)

        sign = request.POST.get('sign')
        item.change_count(sign)

        return JsonResponse({'item': {
            'name': item.product.name,
            'count': item.count,
            'price': item.product.price
        }, 'total_price': cart.get_total_price()})

    return Http404()


def delete_item(request):
    """Delete cart item (ajax)

    POST args:
        product_id (int): Product pk
    Returns:
        JsonResponse | Http404

    """
    if request.method == 'POST' and request.is_ajax():
        product_id = request.POST.get('product_id')
        product = get_object_or_404(Product, pk=product_id)

        cart = Cart.get_cart(request)
        item = get_object_or_404(cart.items, product=product)

        item.delete()

        return JsonResponse({'item': {
            'name': item.product.name
        }, 'total_price': cart.get_total_price()})

    return Http404
