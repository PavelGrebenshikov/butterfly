from django import forms

from .models import Subscription



class SubscriptionForms(forms.ModelForm):

    class Meta:
        model = Subscription
        fields = ("email", )
        widgets = {
            "email": forms.TextInput(attrs={"class": "subscribe__input", "placeholder": "Введите Email"}),
        }
        labels = {
            "email": "",
        }