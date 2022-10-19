import pytest

from butterfly.products.models import Category, Product, Subcategory

pytestmark = pytest.mark.django_db


class TestCategoryModel:
    def test_get_absolute_url(self):

        assert Category.objects.count() == 0
        category = Category.objects.create(name="Category")

        assert Category.objects.count() == 1
        assert category.get_absolute_url() == f"/products/categories/{category.name}"

    def test_category_model_str(self):
        category = Category.objects.create(name="Categories")

        assert category.__str__() == "Categories"

    def test_category_model_count(self):

        assert Category.objects.count() == 0
        Category.objects.create(name="Category")
        assert Category.objects.count() == 1


class TestSubcategoryModel:
    def test_get_absolute_url(self):
        category = Category.objects.create(name="Category")
        subcategory = Subcategory.objects.create(name="Subcategory", category=category)

        assert Category.objects.count() and Subcategory.objects.count() == 1
        assert (
            subcategory.get_absolute_url() == f"/products/categories/{subcategory.name}"
        )

    def test_subcategory_model_str(self):
        category = Category.objects.create(name="Category")
        subcategory = Subcategory.objects.create(name="Subcategory", category=category)

        assert subcategory.__str__() == "Subcategory"

    def test_subcategory_model_count(self):
        category = Category.objects.create(name="Category")

        assert Subcategory.objects.count() == 0
        Subcategory.objects.create(name="Subcategory", category=category)
        assert Subcategory.objects.count() == 1


class TestProductModel:
    def test_product_model_str(self):
        product = Product.objects.create(name="First product", price=20)

        assert product.__str__() == "First product"

    def test_product_model_count(self):

        assert Product.objects.count() == 0
        Product.objects.create(name="Product", price=23)
        assert Product.objects.count() == 1

    def test_get_absolute_url(self):
        product = Product.objects.create(name="Test", price=2333)

        assert product.get_absolute_url() == f"/products/{product.name}"

    @pytest.mark.parametrize(
        "image_url, result",
        [
            ("default.png", "/media/default.png"),
            ("/static/default.png", "/static/default.png"),
        ],
    )
    def test_get_image_url(self, image_url, result):
        product = Product.objects.create(price=0, image_url=image_url)

        assert product.get_image_url() == result
