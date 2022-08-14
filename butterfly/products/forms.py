from django.forms import Form, IntegerField, NumberInput


class ProductsFilterForm(Form):
    price_from = IntegerField(widget=NumberInput(
        attrs={
            'placeholder': 'от'
        }
    ), required=False)
    price_to = IntegerField(widget=NumberInput(
        attrs={
            'placeholder': 'до'
        }
    ), required=False)
