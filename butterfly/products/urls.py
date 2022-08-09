from django.urls import path

from .views import products, product

app_name = 'reviews'
urlpatterns = [
    path('', products, name='all_products'),
    path('<name>', product, name="product_page"),
]
