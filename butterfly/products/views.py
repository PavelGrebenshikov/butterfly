from django.shortcuts import render, get_object_or_404

from products.models import Category, Product, Subcategory


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


def category_products(request, name: str):
    category = Category.objects.filter(name=name).first()
    if not category:
        category = get_object_or_404(Subcategory, name=name)

    context = {
        'categories': Category.objects.all(),
        'products': category.product_set.all()
    }

    return render(request, 'products/products.html', context=context)
