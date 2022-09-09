from django.test import RequestFactory
from django.urls import reverse
import pytest

from butterfly.cart.models import Cart, CartItem
from butterfly.users.tests.factories import UserFactory
from butterfly.products.tests.conftest import created_model_objects

pytestmark = pytest.mark.django_db


class TestCartIndexView():
    fixtures = [created_model_objects]

    def test_anonymous(self, client, created_model_objects):
        cart = Cart.objects.create()
        CartItem.objects.create(product=created_model_objects[0], cart=cart)

        session = client.session
        session['cart_id'] = cart.pk
        session.save()

        response = client.get(reverse('cart:index'))

        assert response.status_code == 200
        assert 'Войдите, чтобы ваша корзина не пропала.' in response.content.decode('utf-8')

    def test_authenticated(self, client):
        user = UserFactory()

        client.force_login(user)

        response = client.get(reverse('cart:index'))

        assert response.status_code == 200
        assert 'Войдите, чтобы ваша корзина не пропала.' not in response.content.decode('utf-8')

    def test_with_products(self, client, rf: RequestFactory, created_model_objects):
        user = UserFactory()
        cart = Cart.objects.create(user=user)
        item = CartItem.objects.create(product=created_model_objects[0], cart=cart)

        client.force_login(user)

        response = client.get(reverse('cart:index'))

        assert response.status_code == 200
        assert item.product.name in response.content.decode('utf-8')


class TestAddToCartView():
    fixtures = [created_model_objects]

    def test_get_request(self, client):
        response = client.get(reverse('cart:add_product'))

        assert response.status_code == 404

    def test_post_request_without_ajax(self, client):
        response = client.post(reverse('cart:add_product'))

        assert response.status_code == 404

    def test_without_product_id(self, client):
        response = client.post(reverse('cart:add_product'),
                               HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        assert response.status_code == 404

    def test_with_wrong_product_id(self, client):
        response = client.post(reverse('cart:add_product'),
                               data={'product_id': 'this is NaN'},
                               HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        assert response.status_code == 404

    def test_with_real_product_id(self, client, created_model_objects):
        response = client.post(reverse('cart:add_product'),
                               data={'product_id': created_model_objects[0].pk},
                               HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        assert response.status_code == 200

        session = client.session
        cart = Cart.objects.get(pk=session.get('cart_id'))
        cart.items.get(product_id=created_model_objects[0].pk)
