from django.db.models import (
    Model,
    EmailField,
    DateTimeField,
    ForeignKey,
    CASCADE,
    BooleanField,
    ManyToManyField,
    CharField,
    TextField,
    SlugField,
)

from django.utils.translation import gettext_lazy as _

from .tasks import mass_send_mail


class Subscription(Model):

    email = EmailField(_("Email"))
    date = DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.email

    class Meta:
        ordering = ["date"]
        app_label = "contact"
        verbose_name = _("Email")
        verbose_name_plural = _("Emails")


class MailSender(Model):
    name = CharField(_("Name"), null=True, max_length=150)
    email = CharField(
        _("E-mail address"),
        max_length=150,
        null=True,
        help_text="Mail for sending messages",
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        app_label = "contact"
        verbose_name = _("Sender")
        verbose_name_plural = _("Senders")


class MailTemplate(Model):
    template = CharField(_("Template"), null=True, blank=True, max_length=150)
    topic = CharField(_("Topic"), null=True, blank=True, max_length=150)
    sender = ForeignKey(MailSender, null=True, blank=True, on_delete=CASCADE)
    message = TextField(_("Message"), null=True, blank=True)
    slug = SlugField(_("Identifier"), null=True, blank=True)

    def __str__(self) -> str:
        return self.template

    class Meta:
        app_label = "contact"
        verbose_name = _("Template")
        verbose_name_plural = _("Templates")


class SendingMessages(Model):
    template = ForeignKey(MailTemplate, on_delete=CASCADE)
    emails = ManyToManyField(Subscription, blank=True)
    send_to_everyone = BooleanField(_("Send to everyone"), default=False)
    date = DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs) -> None:
        if self.send_to_everyone:
            recipients = list(
                Subscription.objects.all().values_list("email", flat=True)
            )
            mass_send_mail.delay(
                self.template.sender.name,
                self.template.message,
                self.template.sender.email,
                recipients,
            )
        return super(SendingMessages, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.template}"

    class Meta:
        ordering = ["date"]
        app_label = "contact"
        verbose_name = _("Sending mail")
        verbose_name_plural = _("Sending mails")
