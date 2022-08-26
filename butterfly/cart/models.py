from django.db.models import (Model, DateTimeField, OneToOneField, CharField, ForeignKey,
                              CASCADE, PositiveSmallIntegerField)

from products.models import Product
from butterfly.users.models import User


class Cart(Model):
    created_at = DateTimeField(auto_now_add=True)
    user = OneToOneField(User, blank=True, null=True, related_name='cart',
                         on_delete=CASCADE, unique=True)

    def __repr__(self):
        return f'<Cart (User {self.user})>'

    def __str__(self):
        return self.__repr__()


class CartItem(Model):
    count = PositiveSmallIntegerField(default=1)
    product = ForeignKey(Product, related_name='cart_items', on_delete=CASCADE)
    cart = ForeignKey(Cart, related_name='items', on_delete=CASCADE)

    def __repr__(self):
        return f'<CartItem (User {self.cart.user})>'

    def __str__(self):
        return self.__repr__()
