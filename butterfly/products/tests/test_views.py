from unicodedata import name
import pytest

from django.urls import reverse

from butterfly.products.models import Product, Category

pytestmark = pytest.mark.django_db


class TestProductsView():
    
    @pytest.fixture
    def created_product_objects(self):
        products = [Product.objects.create(name="first", price=2),
                    Product.objects.create(name="second", price=3)]
        return products
    
    def test_view_all_products(self, client):
        
        url = reverse("products:all_products")
        response = client.get(url)
        
        assert response.status_code == 200
        
    def test_view_product(self, client, created_product_objects):
        url = reverse("products:product_page", args={created_product_objects[0].name})
        response = client.get(url)
        
        assert response.status_code == 200
    
    def test_view_category_products(self, client):
        category = Category.objects.create(name="Category")
        url = reverse("products:category_products", kwargs={"name": category.name})
        response = client.get(url)
        
        assert response.status_code == 200