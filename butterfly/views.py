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

    products = Product.objects.annotate(rank=search_rank).order_by('-rank').values(
        'name', 'price', 'in_stock_count', 'rank')
    context = {
        'products': products,
        'search_product': query
    }
    return render(request, 'products_found.html', context=context)
