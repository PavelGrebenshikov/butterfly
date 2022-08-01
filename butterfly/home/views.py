from django.shortcuts import render

from .models import Category


def index(request):
    context = {
        'categories': Category.objects.all()
    }
    return render(request, 'pages/home.html', context=context)


def products(request):
    context = {
        'categories': Category.objects.all()
    }
    return render(request, 'pages/products.html', context=context)
