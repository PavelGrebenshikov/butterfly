from django.shortcuts import render
from django.contrib.postgres.search import SearchVector, SearchRank

from products.models import Category, Product


def index(request):
    context = {
        'categories': Category.objects.all(),
        'products': Product.objects.all()
    }
    return render(request, 'home.html', context=context)


def search_product(request):
    search_vector = SearchVector('name', 'description')
    query = request.GET.get('q')
    search_rank = SearchRank(search_vector, query)

    products = Product.objects.annotate(rank=search_rank).order_by('-rank').values('name', 'price', 'rank')
    context = {
        'products': products,
        'search_product': query
    }
    
    if query is None:
        return render(request, 'products_found.html', context={'search_product':'Ошибка ввода запроса'})
    return render(request, 'products_found.html', context=context)
