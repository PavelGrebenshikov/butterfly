from unicodedata import category
from django.shortcuts import render
from django.http import request

from .models import Category


def index(request):
    return render(request, 'pages/home.html', context=None)


def products(request):
    context = {
        'categories': Category.objects.all()
    }
    return render(request, 'pages/products.html', context=context)
