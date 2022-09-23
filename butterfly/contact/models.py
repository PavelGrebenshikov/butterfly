from django.db.models import Model, EmailField, DateTimeField

from django.utils.translation import gettext_lazy as _


class Mail(Model):
    # Mail for newsletter

    email = EmailField(_("Email"))
    date = DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.email

    class Meta:
        app_label = "contact"
        verbose_name = _("Email")
        verbose_name_plural = _("Emails")
