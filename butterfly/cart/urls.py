from django.urls import path

from .views import add_product


urlpatterns = [
    path('add-product/', add_product, name='add_product')
]
