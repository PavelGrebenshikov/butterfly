from django.test import RequestFactory
import pytest

from butterfly.cart.models import Cart, CartItem
from butterfly.products.models import Product
from butterfly.products.tests.conftest import created_model_objects
from django.contrib.auth.models import AnonymousUser
from butterfly.users.tests.factories import UserFactory

pytestmark = pytest.mark.django_db


class TestCartModel():
    fixtures = [created_model_objects]

    def test_adding_cart(self):
        user = UserFactory()

        assert Cart.objects.count() == 0
        Cart.objects.create(user=user)
        assert Cart.objects.count() == 1

    def test_authenticated_get_cart(self, rf: RequestFactory):
        request = rf.get('/fake-url/')
        request.user = UserFactory()

        cart = Cart.get_cart(request)
        assert cart.items.count() == 0
        assert cart.user == request.user

    def test_anonymous_get_cart(self, rf: RequestFactory):
        request = rf.get('/fake-url/')
        request.user = AnonymousUser()
        request.session = {}

        cart = Cart.get_cart(request)
        assert cart.items.count() == 0

    def test_get_total_price(self, rf: RequestFactory, created_model_objects):
        request = rf.get('/fake-url/')
        request.user = AnonymousUser()
        request.session = {}

        cart = Cart.get_cart(request)
        cart.save()

        CartItem.objects.create(product=Product.objects.get(price=10), count=3, cart=cart)
        CartItem.objects.create(product=Product.objects.get(price=100), count=1, cart=cart)

        assert cart.get_total_price() == 130
        cart.delete()
