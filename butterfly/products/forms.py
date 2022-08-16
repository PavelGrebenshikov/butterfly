from django.forms import Form, IntegerField, NumberInput, ChoiceField
from django.db.models import QuerySet

from products.models import Product


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

    def get_filtered_products(
            self,
            products: QuerySet = Product.objects.filter(visible=True)) -> QuerySet:
        '''Returns a QuerySet with products filtered by form fields'''

        filtered_products = products.filter(visible=True)
        if self.is_valid():
            price_from = self.cleaned_data['price_from']
            price_to = self.cleaned_data['price_to']

            if price_from is not None:
                filtered_products = filtered_products.filter(price__gte=price_from)
            if price_to is not None:
                filtered_products = filtered_products.filter(price__lte=price_to)

        return filtered_products


class ProductsSortForm(Form):
    sort = ChoiceField(choices=[
        ('price_asc', 'По возрастанию цены'),
        ('price_desc', 'По убыванию цены'),
        ('popular', 'По популярности'),
        ('latest', 'По новизне'),
        ('in_stock_count', 'По количеству товара')
    ])
