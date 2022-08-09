from django.shortcuts import render, get_object_or_404

from products.models import Category, Product


def products(request):
    context = {
        'categories': Category.objects.all(),
        'products': Product.objects.all()[:5]
    }
    return render(request, 'products/products.html', context=context)


def product(request, name: str):
    product = get_object_or_404(Product, name=name)
    context = {
        'product': product
    }
    return render(request, 'products/product.html', context=context)