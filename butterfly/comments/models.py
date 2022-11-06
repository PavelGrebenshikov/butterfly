from django.db.models import (
    Model,
    DateTimeField,
    TextField,
    ForeignKey,
    CASCADE,
    PositiveSmallIntegerField,
)

from butterfly.users.models import User
from butterfly.products.models import Product


class Comment(Model):
    created_at = DateTimeField(auto_now_add=True)
    user = ForeignKey(User, on_delete=CASCADE)
    product = ForeignKey(Product, on_delete=CASCADE)
    text = TextField(null=False)
    rating = PositiveSmallIntegerField(null=True)
