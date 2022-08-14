from django.shortcuts import render, get_object_or_404

from products.models import Category, Product, Subcategory
from .forms import ProductsFilterForm


def products(request):
    form = ProductsFilterForm(request.GET)

    context = {
        'categories': Category.objects.all(),
        'products': form.get_filtered_products(),
        'form': form
    }
    return render(request, 'products/products.html', context=context)


def product(request, name: str):
    product = get_object_or_404(Product, name=name, visible=True)
    context = {
        'product': product
    }
    return render(request, 'products/product.html', context=context)


def category_products(request, name: str):
    category = Category.objects.filter(name=name).first()
    if not category:
        category = get_object_or_404(Subcategory, name=name)

    form = ProductsFilterForm(request.GET)

    context = {
        'categories': Category.objects.all(),
        'products': form.get_filtered_products(category.product_set),
        'form': form
    }

    return render(request, 'products/products.html', context=context)
