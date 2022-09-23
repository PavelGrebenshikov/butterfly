from django.contrib import admin

from .models import Mail

from django.utils.translation import gettext_lazy as _

# Register your models here.


@admin.register(Mail)
class MailAdmin(admin.ModelAdmin):
    list_display = ["email", "date"]
    list_display_links = ["date"]
    list_filter = ["id", "email", "date"]
    search_fields = ["email", "date"]
