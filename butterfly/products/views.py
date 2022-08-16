from django.shortcuts import render, get_object_or_404

from products.models import Category, Product, Subcategory
from .forms import ProductsFilterForm, ProductsSortForm


def products(request):
    filter_form = ProductsFilterForm(request.GET)
    sort_form = ProductsSortForm(request.GET)

    context = {
        'categories': Category.objects.all(),
        'products': filter_form.get_filtered_products(),
        'filter_form': filter_form,
        'sort_form': sort_form
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

    filter_form = ProductsFilterForm(request.GET)
    sort_form = ProductsSortForm(request.GET)

    context = {
        'breadcrumb_obj': category,
        'categories': Category.objects.all(),
        'products': filter_form.get_filtered_products(category.product_set),
        'filter_form': filter_form,
        'sort_form': sort_form
    }

    return render(request, 'products/products.html', context=context)
