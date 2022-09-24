from django.db.models import (
    CASCADE,
    CharField,
    DateTimeField,
    ForeignKey,
    Model,
    PositiveSmallIntegerField,
)

from butterfly.products.models import Product
from butterfly.users.models import User


class Order(Model):
    created_at = DateTimeField(auto_now_add=True)
    user = ForeignKey(User, on_delete=CASCADE)
    status = CharField(max_length=50, default="created")


class OrderItem(Model):
    count = PositiveSmallIntegerField(default=1)
    product = ForeignKey(Product, related_name="order_items", on_delete=CASCADE)
    order = ForeignKey(Order, related_name="items", on_delete=CASCADE)
