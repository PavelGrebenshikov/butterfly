import pytest
from django.urls import reverse

from butterfly.cart.models import Cart, CartItem
from butterfly.orders.models import Order
from butterfly.orders.payment import generate_signature
from butterfly.products.models import Product
from butterfly.products.tests.conftest import created_model_objects
from butterfly.users.tests.factories import UserFactory

pytestmark = pytest.mark.django_db


class TestOrdersIndexView:
    def test_success(self, created_orders: dict[str, Order], client):
        user = created_orders["single product"].user

        client.force_login(user)
        response = client.get(reverse("orders:index"))

        assert response.status_code == 200
        assert f"Заказы ({len(created_orders)})" in response.content.decode("utf-8")


class TestOrderCreateView:
    fixtures = [created_model_objects]

    def test_get(self, client):
        user = UserFactory()

        client.force_login(user)
        response = client.get(reverse("orders:create"))

        assert response.status_code == 404

    def test_with_empty_cart(self, client):
        user = UserFactory()

        client.force_login(user)
        response = client.post(reverse("orders:create"))

        assert response.status_code == 404

    def test_with_cart(self, client, created_model_objects: list[Product]):
        user = UserFactory()
        cart = Cart.objects.create(user=user)
        CartItem.objects.create(cart=cart, product=created_model_objects[0])

        assert Cart.objects.count() == 1
        assert Order.objects.count() == 0

        client.force_login(user)
        response = client.post(reverse("orders:create"))

        assert response.status_code == 302

        assert Cart.objects.count() == 0
        assert Order.objects.count() == 1


class TestApprovePaymentView:
    def test_get(self, client):
        user = UserFactory()

        client.force_login(user)
        response = client.get(reverse("orders:approve_payment"))

        assert response.status_code == 404

    def test_without_signature(self, client):
        user = UserFactory()

        client.force_login(user)
        response = client.post(reverse("orders:approve_payment"))

        assert response.status_code == 404

    def test_with_signature(self, client):
        user = UserFactory()
        order = Order.objects.create(user=user)
        data = {
            "order_id": str(order.unique_id),
            "order_status": "approved",
        }
        signature = generate_signature(data)

        client.force_login(user)
        response = client.post(
            reverse("orders:approve_payment"),
            data={
                **data,
                "signature": signature,
            },
        )

        assert response.status_code == 302
        assert Order.objects.get(unique_id=order.unique_id).status == "approved"
