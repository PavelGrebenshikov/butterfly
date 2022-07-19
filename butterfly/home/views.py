from django.shortcuts import render
from django.http import request

# Create your views here.

def index(request):
    return render(request, 'pages/home.html', context=None)


def products(request):
    return render(request, 'pages/products.html', context=None)