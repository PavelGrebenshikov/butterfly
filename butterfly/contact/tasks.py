from traceback import print_tb
from django.core.mail import send_mass_mail


def mass_send_mail(subject: str, message: str, from_email: str, recipients: list | str):
    send_mass_mail([(subject, message, from_email, recipients)], fail_silently=False)
