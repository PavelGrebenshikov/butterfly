from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.utils.translation import gettext_lazy as _

from butterfly.users.forms import UserAdminChangeForm, UserAdminCreationForm
from butterfly.users.models import User


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):

    form = UserAdminChangeForm
    add_form = UserAdminCreationForm
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            _("Personal info"),
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "email",
                    "city",
                    "date_of_birth",
                    "phone_number",
                    "image_url",
                )
            },
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (
            _("Important dates"),
            {
                "fields": (
                    "last_login",
                    "date_joined",
                    "last_modified",
                ),
            },
        ),
        (
            _("Purchases"),
            {
                "fields": ("favourites",),
            },
        ),
    )
    readonly_fields = ("last_modified",)
    list_display = ["username", "first_name", "last_name", "is_superuser"]
    search_fields = ["name"]

    def cart_items(self, model: User):
        return model.cart.items.all()
