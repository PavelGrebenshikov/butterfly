from email.policy import default
import pytest

from butterfly.products.models import Category, Subcategory, Product

pytestmark = pytest.mark.django_db

class TestCategoryModel():
    
    def test_get_absolute_url(self):
        
        assert Category.objects.count() == 0
        category = Category.objects.create(name="Category")
        
        assert Category.objects.count() == 1
        assert category.get_absolute_url() == f"/products/categories/{category.name}"
        
class TestSubcategoryModel():
    
    def test_get_absolute_url(self):
        
        category = Category.objects.create(name="Category")
        subcategory = Subcategory.objects.create(name="Subcategory", category=category)
        
        assert Category.objects.count() and Subcategory.objects.count() == 1
        assert subcategory.get_absolute_url() == f"/products/categories/{subcategory.name}"

class TestProductModel():
    
    def test_get_absolute_url(self):
        
        assert Product.objects.count() == 0
        product = Product.objects.create(name = "Test", price = 2333)
        
        assert Product.objects.count() == 1
        assert product.get_absolute_url() == f"/products/{product.name}"
    
    @pytest.mark.parametrize("image_url, result", [("default.png", "/media/default.png"),
                                                    ("/static/default.png", "/static/default.png")])
    def test_get_image_url(self, image_url, result):
        product = Product.objects.create(price = 0, image_url = image_url)
        
        assert product.get_image_url() == result