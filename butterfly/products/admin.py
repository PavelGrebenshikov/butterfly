from django.contrib import admin

from .models import Category, Product, Subcategory


class SubcategoryInline(admin.StackedInline):
    model = Subcategory
    extra = 3


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'subcategories_count', 'products_count']
    search_fields = ['name']
    inlines = [SubcategoryInline]

    def subcategories_count(self, model: Category) -> int:
        return model.subcategory_set.count()

    def products_count(self, model: Category) -> int:
        return model.product_set.count()


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'category_name', 'products_count']
    search_fields = ['name']

    def products_count(self, model: Subcategory) -> int:
        return model.product_set.count()

    def category_name(self, model: Subcategory) -> str:
        return model.category.name


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'categories_names']
    search_fields = ['name']

    def categories_names(self, model: Product) -> str:
        categories_set = model.category.all()
        categories_names = [category.name for category in categories_set]
        return ', '.join(categories_names)
