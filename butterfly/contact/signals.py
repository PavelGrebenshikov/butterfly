from django.db.models.signals import m2m_changed
from django.dispatch import receiver

from dbmail import send_db_mail

from .models import SendingMessages

@receiver(m2m_changed, sender=SendingMessages.emails.through)
def send_mail_user(sender, instance, action, *args, **kwargs):
    if action == "post_add":
        if not instance.send_to_everyone:
            send_db_mail(
                instance.template.slug,
                [email for email in instance.emails.all()],
            )
