import pytest
from django.contrib.auth.models import AnonymousUser
from django.http import Http404
from django.test import RequestFactory

from butterfly.cart.models import Cart, CartItem
from butterfly.products.models import Product
from butterfly.products.tests.conftest import created_model_objects
from butterfly.users.tests.factories import UserFactory

pytestmark = pytest.mark.django_db


class TestCartModel:
    fixtures = [created_model_objects]

    def test_adding_cart(self):
        user = UserFactory()

        assert Cart.objects.count() == 0
        Cart.objects.create(user=user)
        assert Cart.objects.count() == 1

    def test_authenticated_get_cart(self, rf: RequestFactory):
        request = rf.get("/fake-url/")
        request.user = UserFactory()

        cart = Cart.get_cart(request)
        assert cart.items.count() == 0
        assert cart.user == request.user

    def test_anonymous_get_cart(self, rf: RequestFactory):
        request = rf.get("/fake-url/")
        request.user = AnonymousUser()
        request.session = {}

        cart = Cart.get_cart(request)
        assert cart.items.count() == 0

    def test_get_total_price(self, created_model_objects):

        cart = Cart.objects.create()

        CartItem.objects.create(
            product=Product.objects.get(price=10), count=3, cart=cart
        )
        CartItem.objects.create(
            product=Product.objects.get(price=100), count=1, cart=cart
        )

        assert cart.get_total_price() == 130


class TestCartItemModel:
    fixtures = [created_model_objects]

    def test_adding_cart_item(self, created_model_objects):
        cart = Cart.objects.create()

        assert CartItem.objects.count() == 0
        CartItem.objects.create(product=Product.objects.get(name="First"), cart=cart)
        assert CartItem.objects.count() == 1

    def test_can_change_count_returns_false(self, created_model_objects):
        cart = Cart.objects.create()

        item = CartItem(product=Product.objects.get(name="First"), cart=cart, count=1)

        assert not item._can_change_count("-")

        item.count = 20

        assert not item._can_change_count("+")

    def test_can_chnage_count_returns_true(self, created_model_objects):
        cart = Cart.objects.create()

        item = CartItem(product=Product.objects.get(name="First"), cart=cart, count=2)

        assert item._can_change_count("+")
        assert item._can_change_count("-")

    def test_change_count_successfully_changes(self, created_model_objects):
        cart = Cart.objects.create()

        item = CartItem(product=Product.objects.get(name="First"), cart=cart, count=2)
        assert item.count == 2
        item.change_count("+")
        assert item.count == 3
        item.change_count("-")
        assert item.count == 2

    def test_change_count_dont_changes(self, created_model_objects):
        cart = Cart.objects.create()

        item = CartItem(product=Product.objects.get(name="First"), cart=cart, count=1)
        item.change_count("-")
        assert item.count == 1

        item.count = 20

        item.change_count("+")
        assert item.count == 20

    def test_change_count_raises_http404(self, created_model_objects):
        cart = Cart.objects.create()

        item = CartItem(product=Product.objects.get(name="First"), cart=cart, count=1)

        with pytest.raises(Http404):
            item.change_count("Just wrong argument!")
