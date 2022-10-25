from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views import defaults as default_views

from butterfly.views import index, search_product

urlpatterns = [
    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),
    # Apps' views
    path("users/", include("butterfly.users.urls", namespace="users")),
    path("accounts/", include("allauth.urls")),
    path("products/", include("butterfly.products.urls", namespace="products")),
    path("cart/", include(("butterfly.cart.urls", "butterfly.cart"), namespace="cart")),
    path("orders/", include("butterfly.orders.urls", namespace="orders")),
    path("contact/", include(("butterfly.contact.urls", "butterfly.contact"), namespace="contact")),
    path("favourites/", include("butterfly.favourites.urls", namespace="favourites")),
    # Global views
    path("search/", search_product, name="search_product"),
    path("index/", index, name="index"),
    path("", index, name="home")
    # Your stuff: custom urls includes go here
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
