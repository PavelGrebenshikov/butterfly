from django.urls import include, path

# here import from views.py functions
from .views import index, products

urlpatterns = [
    path('index/', index, name="home"),
    path('products/', products, name="products")
] 