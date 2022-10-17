from django.urls import path

from .views import approve_payment, create, index

app_name = "orders"
urlpatterns = [
    path("", index, name="index"),
    path("create/", create, name="create"),
    path("approve-payment/", approve_payment, name="approve_payment"),
]
