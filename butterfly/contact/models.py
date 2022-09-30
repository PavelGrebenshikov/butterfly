from django.db.models import Model, EmailField, DateTimeField, ForeignKey, CASCADE, BooleanField, ManyToManyField

from django.utils.translation import gettext_lazy as _


from dbmail.models import MailTemplate
from dbmail import send_db_mail

class Subscription(Model):
    # Mail for newsletter

    email = EmailField(_("Email"))
    date = DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.email

    class Meta:
        app_label = "contact"
        verbose_name = _("Email")
        verbose_name_plural = _("Emails")

class SendingMessages(Model):
    template = ForeignKey(MailTemplate, on_delete=CASCADE)
    emails = ManyToManyField(Subscription, blank=True)
    send_to_everyone = BooleanField(default=False)
    use_celery = BooleanField(default=False)

    def save(self, *args, **kwargs):
        recipients = list(Subscription.objects.all().values_list("email", flat=True))
        if self.send_to_everyone:
            send_db_mail(
                self.template.slug,
                recipients,
            )
        return super(SendingMessages, self).save(*args, **kwargs)

    class Meta:
        app_label = "contact"
        verbose_name = "Отправка сообщения"
        verbose_name_plural = "Отправка сообщений"
