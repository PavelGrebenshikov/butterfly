from django.db.models import (Model, DateTimeField, OneToOneField, ForeignKey,
                              CASCADE, PositiveSmallIntegerField)
from django.http import HttpRequest

from butterfly.users.models import User
from products.models import Product


class Cart(Model):
    created_at = DateTimeField(auto_now_add=True)
    user = OneToOneField(User, blank=True, null=True, related_name='cart',
                         on_delete=CASCADE, unique=True)

    @staticmethod
    def get_cart(request: HttpRequest) -> 'Cart':
        '''Returns a Cart object by request.user'''

        if request.user.is_authenticated:
            cart, _ = Cart.objects.get_or_create(user=request.user)
        else:
            try:
                cart = Cart.objects.get(
                    pk=request.session.get('cart_id')
                )

            except Cart.DoesNotExist:
                cart = Cart(user=None)

        return cart

    def __repr__(self):
        return f'<Cart (User {self.user})>'

    def __str__(self):
        '''Django uses __str__ method in django-admin
        and we must implicitly define this method'''
        return self.__repr__()


class CartItem(Model):
    count = PositiveSmallIntegerField(default=1)
    product = ForeignKey(Product, related_name='cart_items', on_delete=CASCADE)
    cart = ForeignKey(Cart, related_name='items', on_delete=CASCADE)

    def __repr__(self):
        return f'<CartItem (User {self.cart.user})>'

    def __str__(self):
        return self.__repr__()
