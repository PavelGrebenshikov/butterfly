from django.db.models.signals import m2m_changed
from django.dispatch import receiver

from django.conf import settings
from django.core.mail import send_mail, send_mass_mail

from django.utils.translation import gettext_lazy as _

from .models import SendMail, Mail


@receiver(m2m_changed, sender=SendMail.emails.through)
def send_mail_user(sender, instance, action, *args, **kwargs):
    if action == "post_add":
        if not instance.choice:
            send_mail(
                str(instance.subject),
                str(instance.message),
                settings.EMAIL_HOST_USER,
                [email for email in instance.emails.all()],
                fail_silently=False
            )
        else:
            emails = Mail.objects.only("email")
            reciever_list = [str(email) for email in emails]
            datatuple = (
                str(instance.subject),
                str(instance.message),
                settings.EMAIL_HOST_USER,
                reciever_list
            )
            send_mass_mail((datatuple, ), fail_silently=False)
