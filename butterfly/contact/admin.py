from django.contrib import admin
from django.conf import settings

from .models import Mail, SendMail

from django.utils.translation import gettext_lazy as _

# Register your models here.

@admin.register(SendMail)
class SendMailAdmin(admin.ModelAdmin):
    list_display = ['message',]

@admin.register(Mail)
class MailAdmin(admin.ModelAdmin):
    list_display = ['email', 'date']
    list_display_links = ['date']
    list_filter = ['id', 'email', 'date']
    search_fields = ['email', 'date']
    