from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, TextField, DateField, DateTimeField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """
    Default custom user model for Butterfly.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    city = CharField(max_length=50, blank=True)
    date_of_birth = DateField(null=True)
    phone_number = CharField(max_length=20, blank=True)
    last_modified = DateTimeField(auto_now=True)
    image_url = TextField(default='/static/profile.png')

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
