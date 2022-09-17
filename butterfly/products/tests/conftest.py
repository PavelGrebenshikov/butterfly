import pytest

from butterfly.products.models import Product


@pytest.fixture
def created_model_objects():
    products = [
        Product.objects.create(name="First", price=10, visible=True, in_stock_count=20),
        Product.objects.create(name="Second", price=50, visible=True),
        Product.objects.create(name="Third", price=100, visible=True),
    ]
    return products
