from django.urls import path

from .views import all_products, product, category_products

app_name = 'reviews'
urlpatterns = [
    path('', all_products, name='all_products'),
    path('categories/<name>', category_products, name='category_products'),
    path('<name>', product, name="product_page")
]
