import pytest

from butterfly.orders.models import Order

pytestmark = pytest.mark.django_db


class TestOrderModel:
    def test_get_amount(self, created_orders: dict[str, Order]):
        assert created_orders["many products"].get_amount() == 100 + 50 + 10
