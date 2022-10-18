from django.urls import path

from .views import add_product

app_name = "favourites"
urlpatterns = [
    path("add-product/", add_product, name="add_product"),
]
