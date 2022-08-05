from django.shortcuts import render

from .models import Category, Product


def index(request):
    context = {
        'categories': Category.objects.all(),
        'products': Product.objects.all()
    }
    return render(request, 'home/home.html', context=context)


def products(request):
    context = {
        'categories': Category.objects.all(),
        'products': Product.objects.all()[:5]
    }
    return render(request, 'home/products.html', context=context)
