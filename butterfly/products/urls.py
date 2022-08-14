from django.urls import path

from .views import filtered_products, product, category_products

app_name = 'reviews'
urlpatterns = [
    path('', filtered_products, name='all_products'),
    path('categories/<name>', category_products, name='category_products'),
    path('<name>', product, name="product_page")
]
