from itertools import product
import pytest

from django.forms import Form

from butterfly.products.models import Product
from butterfly.products.forms import ProductsFilterForm, ProductsSortForm

pytestmark = pytest.mark.django_db


class TestProductsFilterForm():
    
    @pytest.fixture
    def created_model_objects(self):
        products =  [
            Product.objects.create(name="First", price=10, visible=True),
            Product.objects.create(name="Second", price=50, visible=True),
            Product.objects.create(name="Third", price=100, visible=True)
        ]
        return products
    
    @pytest.mark.parametrize("min_price, max_price", [(40, 150)])
    def test_filtred_products(self, created_model_objects, min_price, max_price):
        
        form_data = {"price_from": min_price, "price_to": max_price}
        
        form = ProductsFilterForm(form_data)
        
        assert form.is_valid() == True
        assert len(form.get_filtered_products()) == 2
        assert form.get_filtered_products()[0].name == "Second" and \
            form.get_filtered_products()[1].name == "Third"

class TestProductsSortForm():
    
    @pytest.fixture
    def created_model_objects(self):
        products = [
            Product.objects.create(name="First", price=10, visible=True),
            Product.objects.create(name="Second", price=50, visible=True),
            Product.objects.create(name="Third", price=100, visible=True)
        ]
        return products
    
    @pytest.mark.parametrize("test_sort, price, product_name", [("sort", "price_desc", "Third"),
                                                                ("sort", "price_asc", "First"),])
    def test_sorted_products(self, created_model_objects, test_sort, price, product_name):
        
        form_data = {test_sort: price}
        
        form = ProductsSortForm(form_data)
        
        assert form.is_valid() == True
        assert len(form.get_sorted_products()) == 3
        assert form.get_sorted_products()[0].name == product_name