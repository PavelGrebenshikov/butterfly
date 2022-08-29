from django.urls import path

from .views import add_product, change_item_count, index


urlpatterns = [
    path('', index, name='index'),
    path('add-product/', add_product, name='add_product'),
    path('change-item-count/', change_item_count, name='change_item_count')
]
