from django.db.models import (
    Model, CharField, TextField, BooleanField,
    DecimalField, DateTimeField, ForeignKey, ManyToManyField,
    ImageField, CASCADE
)
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Category(Model):

    name = CharField(_('Name of category'), max_length=30)

    def __repr__(self):
        return f'<Category {self.name}>'

    class Meta:
        app_label = 'home'
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


class Subcategory(Model):
    category = ForeignKey(Category, on_delete=CASCADE)
    name = CharField(_('Name of subcategory'), max_length=50)

    def __repr__(self):
        return f'<Subcategory {self.name}>'

    class Meta:
        app_label = 'home'
        verbose_name = _('Subcategory')
        verbose_name_plural = _('Subcategories')


class Product(Model):
    name = CharField(_('Product name'), max_length=100)
    description = TextField(_('Description'), blank=True)
    price = DecimalField(_('Price'), max_digits=5, decimal_places=2)
    created_at = DateTimeField(_('Creation date'), auto_now_add=True)
    last_modified = DateTimeField(_('Last modifying'), auto_now=True)
    visible = BooleanField(_('Is visible'), default=True)
    image_url = ImageField(_('Image url'), upload_to='products/photos/', default='/static/images/product.png')

    category = ManyToManyField(Category)
    subcategory = ManyToManyField(Subcategory)

    def __repr__(self):
        return f'<Product {self.name}>'

    def get_absolute_url(self):
        """
        NOTE: This is real product url. But now we are using fictive url.

        return reverse("products:detail", kwargs={"name": self.name})
        """
        return '#'

    def get_image_url(self):
        if str(self.image_url).startswith('/static'):
            return self.image_url
        else:
            return f'/media/{self.image_url}'

    class Meta:
        app_label = 'home'
