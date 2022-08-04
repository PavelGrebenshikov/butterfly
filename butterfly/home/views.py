from django.shortcuts import render

from .models import Category


def index(request):
    context = {
        'categories': Category.objects.all()
    }
    return render(request, 'home/home.html', context=context)


def products(request):
    context = {
        'categories': Category.objects.all()
    }
    return render(request, 'home/products.html', context=context)
