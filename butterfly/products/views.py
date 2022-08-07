from django.shortcuts import render

from products.models import Category, Product


def products(request):
    context = {
        'categories': Category.objects.all(),
        'products': Product.objects.all()[:5]
    }
    return render(request, 'products/products.html', context=context)
