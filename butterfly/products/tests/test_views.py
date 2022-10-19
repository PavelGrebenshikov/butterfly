import pytest
from django.urls import reverse

from butterfly.products.models import Category

pytestmark = pytest.mark.django_db


class TestProductsView:
    def test_view_all_products(self, client):

        url = reverse("products:all_products")
        response = client.get(url)

        assert response.status_code == 200

    def test_view_product(self, client, created_model_objects):
        url = reverse("products:product_page", args={created_model_objects[0].name})
        response = client.get(url)

        assert response.status_code == 200

    def test_view_category_products(self, client):
        category = Category.objects.create(name="Category")
        url = reverse("products:category_products", kwargs={"name": category.name})
        response = client.get(url)

        assert response.status_code == 200
