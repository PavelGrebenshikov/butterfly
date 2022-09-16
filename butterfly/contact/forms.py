from django import forms

from .models import Mail



class SubscriptionForms(forms.ModelForm):

    class Meta:
        model = Mail
        fields = ("email", )
        widgets = {
            "email": forms.TextInput(attrs={"class": "subscribe__input", "placeholder": "Введите Email"}),
        }
        labels = {
            "email": "",
        }