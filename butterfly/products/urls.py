from django.urls import path

from .views import products, product

urlpatterns = [
    path('', products, name='all_products'),
    path('product/<pk>', product, name="product_page"),
]
