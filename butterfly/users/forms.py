from allauth.account.forms import SignupForm
from allauth.socialaccount.forms import SignupForm as SocialSignupForm
from django.contrib.auth import forms as admin_forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.forms import CharField, DateField, RegexField, TextInput, SelectDateWidget

User = get_user_model()


class UserAdminChangeForm(admin_forms.UserChangeForm):
    class Meta(admin_forms.UserChangeForm.Meta):
        model = User


class UserAdminCreationForm(admin_forms.UserCreationForm):
    """
    Form for User Creation in the Admin Area.
    To change user signup, see UserSignupForm and UserSocialSignupForm.
    """

    class Meta(admin_forms.UserCreationForm.Meta):
        model = User

        error_messages = {
            "username": {"unique": _("This username has already been taken.")}
        }


class UserSignupForm(SignupForm):
    """
    Form that will be rendered on a user sign up section/screen.
    Default fields will be added automatically.
    Check UserSocialSignupForm for accounts created from social.
    """

    first_name = CharField(widget=TextInput(
        attrs={
            'placeholder': _('First name'),
            'autocomplete': 'city'
        }))
    last_name = CharField(widget=TextInput(
        attrs={
            'placeholder': _('Last name'),
            'autocomplete': 'city'
        }))
    city = CharField(widget=TextInput(
        attrs={
            'placeholder': _('City (optional)'),
            'autocomplete': 'city'
        }
    ), required=False)
    date_of_birth = DateField(label=_('Date of birth (optional)'), widget=SelectDateWidget(years=range(2010, 1920, -1)))
    phone_number = RegexField(widget=TextInput(
        attrs={
            'placeholder': _('Phone number (optional)'),
            'autocomplete': 'phone'
        }),
        regex=r'^\+?\d{1,3}\s?\(?\d{3}\)?\s?\d{3}[- ]?\d{2}[- ]?\d{2}$',
        required=False)

    def save(self, request):
        user = super(UserSignupForm, self).save(request)

        user.city = self.cleaned_data['city']
        user.date_of_birth = self.cleaned_data['date_of_birth']
        user.phone_number = self.cleaned_data['phone_number']

        user.save()
        return user


class UserSocialSignupForm(SocialSignupForm):
    """
    Renders the form when user has signed up using social accounts.
    Default fields will be added automatically.
    See UserSignupForm otherwise.
    """
