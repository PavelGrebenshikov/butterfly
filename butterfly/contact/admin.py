from django.contrib import admin

from .models import Subscription, SendingMessages, MailSender, MailTemplate

from django.utils.translation import gettext_lazy as _

# Register your models here.


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ["email", "date"]
    list_display_links = ["date"]
    list_filter = ["id", "email", "date"]
    search_fields = ["email", "date"]


@admin.register(MailSender)
class MailSenderAdmin(admin.ModelAdmin):
    list_display = ["name", "email"]


@admin.register(MailTemplate)
class MailTemplateAdmin(admin.ModelAdmin):
    list_display = ["template", "topic", "sender", "message", "slug"]
    prepopulated_fields = {"slug": ("template",)}


@admin.register(SendingMessages)
class SendingMessages(admin.ModelAdmin):
    autocomplete_fields = ["emails"]
