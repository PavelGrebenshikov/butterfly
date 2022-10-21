from django.db.models import (
    CASCADE,
    DateTimeField,
    ForeignKey,
    Model,
    OneToOneField,
    PositiveSmallIntegerField,
)
from django.http import HttpResponseBadRequest, HttpRequest
from butterfly.exceptions import HttpErrorException

from butterfly.products.models import Product
from butterfly.users.models import User


class Cart(Model):
    created_at = DateTimeField(auto_now_add=True)
    user = OneToOneField(
        User, blank=True, null=True, related_name="cart", on_delete=CASCADE, unique=True
    )

    @staticmethod
    def get_cart(request: HttpRequest) -> "Cart":
        """Returns a Cart object by request.user or cart id in request.session"""

        if request.user.is_authenticated:
            cart, _ = Cart.objects.get_or_create(user=request.user)
        else:
            try:
                cart = Cart.objects.get(pk=request.session.get("cart_id"))

            except Cart.DoesNotExist:
                cart = Cart(user=None)
                cart.save()

        return cart

    def get_total_price(self):
        """Returns total price of all items in cart"""
        return sum(item.product.price * item.count for item in self.items.all())

    def __repr__(self):
        return f"<Cart (User {self.user})>"

    def __str__(self):
        """Django uses __str__ method in django-admin
        and we must implicitly define this method"""
        return self.__repr__()


class CartItem(Model):
    count = PositiveSmallIntegerField(default=1)
    product = ForeignKey(Product, related_name="cart_items", on_delete=CASCADE)
    cart = ForeignKey(Cart, related_name="items", on_delete=CASCADE)

    def change_count(self, sign: str) -> None:
        """Changes count field by sign

        Args:
            sign ('+' or '-'): Increment (+) or decrement (-) value

        Raises:
            Http404: If sign not '+' or not '-'
        """
        if self._can_change_count(sign):
            match sign:
                case "+":
                    self.count += 1
                case "-":
                    self.count -= 1
                case _:
                    raise HttpErrorException(400)

            self.save()

    def _can_change_count(self, sign: str) -> bool:
        """Checks that count can be changed by sign.
        That means 1 <= new count <= product stock count.

        Args:
            sign ('+' or '-'): New count will be incremented (+) or decremented (-)

        Returns:
            bool
        """
        match sign:
            case "+":
                if self.product.in_stock_count <= self.count:
                    return False

            case "-":
                if self.count <= 1:
                    return False

        return True

    def __repr__(self):
        return f"<CartItem (User {self.cart.user})>"

    def __str__(self):
        return self.__repr__()
