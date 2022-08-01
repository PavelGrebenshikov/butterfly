from django.urls import path

from .views import index, products

urlpatterns = [
    path('', index, name='home'),
    path('index/', index, name="home"),
    path('products/', products, name="products")
]
