from django.contrib import admin

from .models import Category, Subcategory


class SubcategoryInline(admin.StackedInline):
    model = Subcategory
    extra = 3


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'subcategories_count']
    search_fields = ['name']
    inlines = [SubcategoryInline]

    def subcategories_count(self, model: Category) -> int:
        return len(model.subcategory_set.all())


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']
    search_fields = ['name']
