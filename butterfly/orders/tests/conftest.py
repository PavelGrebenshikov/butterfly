import pytest

from butterfly.orders.models import Order
from butterfly.products.tests.conftest import created_model_objects
from butterfly.users.tests.factories import UserFactory

fixtures = [created_model_objects]


@pytest.fixture
def created_orders(created_model_objects: list) -> dict[str, Order]:
    user = UserFactory()

    orders = {
        "single product": Order.objects.create(user=user),
        "two products": Order.objects.create(user=user),
        "many products": Order.objects.create(user=user),
    }

    orders["single product"].items.create(product=created_model_objects[0])

    orders["two products"].items.create(product=created_model_objects[0])
    orders["two products"].items.create(product=created_model_objects[1])

    orders["many products"].items.create(product=created_model_objects[0])
    orders["many products"].items.create(product=created_model_objects[1])
    orders["many products"].items.create(product=created_model_objects[2])

    return orders
