from django.shortcuts import render, get_object_or_404

from products.models import Category, Product, Subcategory
from .forms import ProductsFilterForm


def filtered_products(request):
    form = ProductsFilterForm(request.GET)
    if form.is_valid():
        price_from = form.cleaned_data['price_from']
        price_to = form.cleaned_data['price_to']

        filtered_products = Product.objects.filter(visible=True)
        if price_from is not None:
            filtered_products = filtered_products.filter(price__gte=price_from)
        if price_to is not None:
            filtered_products = filtered_products.filter(price__lte=price_to)

    context = {
        'categories': Category.objects.all(),
        'products': filtered_products,
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

    context = {
        'categories': Category.objects.all(),
        'products': category.product_set.filter(visible=True)
    }

    return render(request, 'products/products.html', context=context)
