from django.contrib.auth.models import AbstractUser
from django.db.models import (
    CharField,
    DateField,
    DateTimeField,
    ImageField,
    ManyToManyField,
)
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from butterfly.products.models import Product


class User(AbstractUser):
    """
    Default custom user model for Butterfly.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    city = CharField(_("City"), max_length=50, blank=True)
    date_of_birth = DateField(_("Date of birth"), null=True)
    phone_number = CharField(_("Phone number"), max_length=20, blank=True)
    last_modified = DateTimeField(auto_now=True)
    image_url = ImageField(
        _("Image url"), upload_to="users/avatars/", default="/static/images/profile.png"
    )

    favourites = ManyToManyField(Product)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})

    def __repr__(self):
        return f"<User {self.username}>"

    def __str__(self):
        return self.username
