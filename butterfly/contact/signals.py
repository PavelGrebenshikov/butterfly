from django.db.models.signals import m2m_changed
from django.dispatch import receiver

from django.core.mail import send_mail, BadHeaderError
from .models import SendingMessages


@receiver(m2m_changed, sender=SendingMessages.emails.through)
def send_mail_user(sender, instance, action, *args, **kwargs):
    if action == "post_add":
        if not instance.send_to_everyone:
            send_mail(
                instance.template.sender.name,
                instance.template.message,
                instance.template.sender.email,
                list(instance.emails.all()),
                fail_silently=False,
            )
