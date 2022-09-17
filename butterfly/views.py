from django.contrib.postgres.search import SearchRank, SearchVector
from django.shortcuts import render

from butterfly.cart.models import Cart
from butterfly.products.models import Category, Product


def index(request):
    cart_products_ids = [item.product.pk for item in Cart.get_cart(request).items.all()]

    context = {
        "categories": Category.objects.all(),
        "products": Product.objects.filter(visible=True)[:5],
        "cart_products_ids": cart_products_ids,
    }
    return render(request, "home.html", context=context)


def search_product(request):
    search_vector = SearchVector("name", "description")
    query = request.GET.get("q")
    search_rank = SearchRank(search_vector, query)

    products = (
        Product.objects.annotate(rank=search_rank)
        .filter(visible=True)
        .order_by("-rank")
        .values("name", "price", "in_stock_count", "rank")
    )
    context = {"products": products, "search_product": query}
    return render(request, "products_found.html", context=context)
