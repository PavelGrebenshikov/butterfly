from django.urls import include, path

# here import from views.py functions
from .views import index

urlpatterns = [
    path('', index, name="home"),
] 