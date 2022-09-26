from django.urls import path

from .views import create


app_name = "orders"
urlpatterns = [path("create/", create, name="create")]
