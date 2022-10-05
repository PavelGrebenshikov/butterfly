from django.db.models import (
    CASCADE,
    CharField,
    DateTimeField,
    ForeignKey,
    Model,
    PositiveSmallIntegerField,
    UUIDField,
)
import uuid

from butterfly.products.models import Product
from butterfly.users.models import User


class Order(Model):
    unique_id = UUIDField(default=uuid.uuid4, editable=False)
    created_at = DateTimeField(auto_now_add=True)
    user = ForeignKey(User, related_name="orders", on_delete=CASCADE)
    status = CharField(max_length=50, default="created")

    def get_amount(self) -> int:
        """Returns order amount"""
        return sum(item.product.price * item.count for item in self.items.all())

    def __repr__(self):
        return f"<Order (User {self.user}) ({self.items.count()} products)>"

    def __str__(self):
        return self.__repr__()


class OrderItem(Model):
    count = PositiveSmallIntegerField(default=1)
    product = ForeignKey(Product, related_name="order_items", on_delete=CASCADE)
    order = ForeignKey(Order, related_name="items", on_delete=CASCADE)

    def __repr__(self):
        return f"<Order item ({self.product})>"

    def __str__(self):
        return self.__repr__()
