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
        app_label = "contact"
        verbose_name = _("Email")
        verbose_name_plural = _("Emails")


class MailSender(Model):
    name = CharField(_("Название"), null=True, max_length=150)
    email = CharField(
        _("Адрес электронной почты"),
        max_length=150,
        null=True,
        help_text="Почта для отправки сообщений",
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        app_label = "contact"
        verbose_name = _("Sender")
        verbose_name_plural = _("Senders")


class MailTemplate(Model):
    template = CharField(_("Шаблон"), null=True, blank=True, max_length=150)
    topic = CharField(_("Тема"), null=True, blank=True, max_length=150)
    sender = ForeignKey(MailSender, null=True, blank=True, on_delete=CASCADE)
    message = TextField(_("Сообщение"), null=True, blank=True)
    slug = SlugField(_("Индефикатор"), null=True, blank=True)

    def __str__(self) -> str:
        return self.template

    class Meta:
        app_label = "contact"
        verbose_name = _("Template")
        verbose_name_plural = _("Templates")


class SendingMessages(Model):
    template = ForeignKey(MailTemplate, on_delete=CASCADE)
    emails = ManyToManyField(Subscription, blank=True)
    send_to_everyone = BooleanField(_("Отправить всем"), default=False)

    def save(self, *args, **kwargs) -> None:
        if self.send_to_everyone:
            recipients = list(
                Subscription.objects.all().values_list("email", flat=True)
            )
            mass_send_mail(
                self.template.sender.name,
                self.template.message,
                self.template.sender.email,
                recipients,
            )
        return super(SendingMessages, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.template}"

    class Meta:
        app_label = "contact"
        verbose_name = "Sending mail"
        verbose_name_plural = "Sending mails"
