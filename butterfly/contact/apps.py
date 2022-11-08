from django.apps import AppConfig


class ContactConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "butterfly.contact"

    def ready(self):
        import butterfly.contact.signals