from django.urls import path

from .views import products, product, category_products

app_name = 'reviews'
urlpatterns = [
    path('', products, name='all_products'),
    path('categories/<name>', category_products, name='category_products'),
    path('<name>', product, name="product_page")
]
