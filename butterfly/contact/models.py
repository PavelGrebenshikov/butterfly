from tabnanny import verbose
from django.db.models import (
    Model, EmailField, DateTimeField
)

class Subscription(Model):
    # Mail newsletter subscription

    email = EmailField(_("Email"))
    date = DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.email

    class Meta:
        app_label = "contact"
        verbose_name = _("Email")
        verbose_name_plural = _("Emails")