import pytest

from django.urls import resolve, reverse

from butterfly.products.models import Product, Category

pytestmark = pytest.mark.django_db

def test_category_url():
    
    category = Category.objects.create(name = "Category")
    
    assert reverse("products:category_products", kwargs={"name": category.name})
    assert resolve(f"/products/categories/{category.name}").view_name == "products:category_products"
    
def test_product_url():
    
    product = Product.objects.create(name = "Product", price = 404)
    
    assert reverse("products:product_page", kwargs={"name": product.name})
    assert resolve(f"/products/{product.name}").view_name == "products:product_page"
