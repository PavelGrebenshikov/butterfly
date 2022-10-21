from django.shortcuts import reverse
import pytest

from butterfly.products.tests.conftest import created_model_objects
from butterfly.users.tests.factories import UserFactory

pytestmark = pytest.mark.django_db


class TestIndexFavouritesView:
    def test_success(self, client):
        user = UserFactory()
        client.force_login(user)
        response = client.get(reverse("favourites:index"))

        assert response.status_code == 200


class TestAddToFavouritesView:
    fixtures = [created_model_objects]

    def test_get_request(self, client):
        user = UserFactory()
        client.force_login(user)
        response = client.get(reverse("favourites:add_product"))

        assert response.status_code == 405

    def test_post_request_without_ajax(self, client):
        user = UserFactory()
        client.force_login(user)
        response = client.post(reverse("favourites:add_product"))

        assert response.status_code == 405

    def test_without_product_id(self, client):
        user = UserFactory()
        client.force_login(user)
        response = client.post(
            reverse("favourites:add_product"),
            HTTP_X_REQUESTED_WITH="XMLHttpRequest",
        )

        assert response.status_code == 400

    def test_with_wrong_product_id(self, client):
        user = UserFactory()
        client.force_login(user)
        response = client.post(
            reverse("favourites:add_product"),
            data={"product_id": "this is NaN"},
            HTTP_X_REQUESTED_WITH="XMLHttpRequest",
        )

        assert response.status_code == 400

    def test_with_real_product_id(self, client, created_model_objects):
        user = UserFactory()
        client.force_login(user)
        response = client.post(
            reverse("favourites:add_product"),
            data={"product_id": created_model_objects[0].pk},
            HTTP_X_REQUESTED_WITH="XMLHttpRequest",
        )

        assert response.status_code == 200
        assert response.json()["product"]["name"] == created_model_objects[0].name
        assert response.json()["cart_total_price"] == 0
        assert user.favourites.count() == 1
