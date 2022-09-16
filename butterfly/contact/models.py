from django.db.models import (
    Model, EmailField, DateTimeField, TextField, BooleanField, CharField,
    ManyToManyField,
)

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

class SendMail(Model):
    # Model for Sending mailing list

    subject = CharField(_("Subject"), max_length=128)
    message = TextField(_("Message to send"))
    emails = ManyToManyField(Mail, blank=True)
    choice = BooleanField(_("Send to all users"), default=False)
    date = DateTimeField(_("Date of creation"), auto_now_add=True)

    def __str__(self) -> str:
        return self.message
    class Meta:
        app_label = "contact"
        verbose_name = _("Sending to Mail")
        verbose_name_plural = _("Sending to Mail")
