from django.contrib import admin
from .models import Subscription

# Register your models here.


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['email', 'date']
    list_display_links = ['date']
    search_fields = ['email', 'date']
