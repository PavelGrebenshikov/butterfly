from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, ImageField, DateField, DateTimeField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """
    Default custom user model for Butterfly.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    city = CharField(_('City'), max_length=50, blank=True)
    date_of_birth = DateField(_('Date of birth'), null=True)
    phone_number = CharField(_('Phone number'), max_length=20, blank=True)
    last_modified = DateTimeField(auto_now=True)
    image_url = ImageField(_('Image url'), upload_to='users/avatars/', default='/static/images/profile.png')

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
