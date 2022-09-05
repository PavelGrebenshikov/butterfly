from django.db.models import (
    Model, CharField, TextField, BooleanField,
    DecimalField, DateTimeField, ForeignKey, ManyToManyField,
    ImageField, PositiveSmallIntegerField, CASCADE
)
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Category(Model):

    name = CharField(_('Name of category'), max_length=30)
    
    def __str__(self):
        return self.name

    def __repr__(self):
        return f'<Category {self.name}>'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("products:category_products", kwargs={'name': self.name})

    class Meta:
        app_label = 'products'
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


class Subcategory(Model):
    category = ForeignKey(Category, on_delete=CASCADE)
    name = CharField(_('Name of subcategory'), max_length=50)
    
    def __str__(self):
        return self.name

    def __repr__(self):
        return f'<Subcategory {self.name}>'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("products:category_products", kwargs={'name': self.name})

    class Meta:
        app_label = 'products'
        verbose_name = _('Subcategory')
        verbose_name_plural = _('Subcategories')


class Product(Model):
    name = CharField(_('Product name'), max_length=100)
    description = TextField(_('Description'), blank=True)
    price = DecimalField(_('Price'), max_digits=7, decimal_places=2)
    created_at = DateTimeField(_('Creation date'), auto_now_add=True)
    last_modified = DateTimeField(_('Last modifying'), auto_now=True)
    visible = BooleanField(_('Is visible'), default=True)
    image_url = ImageField(_('Image url'), upload_to='products/photos/', default='/static/images/product.png')
    format = CharField(_('Product format'), max_length=100, blank=True)
    vendor_code = CharField(_('Vendor code'), max_length=50)
    in_stock_count = PositiveSmallIntegerField(_('Products in stock'), default=0)

    category = ManyToManyField(Category)
    subcategory = ManyToManyField(Subcategory)
    
    def __str__(self):
        return self.name

    def __repr__(self):
        return f'<Product {self.name}>'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("products:product_page", kwargs={'name': self.name})

    def get_image_url(self):
        if str(self.image_url).startswith('/static'):
            return self.image_url
        else:
            return f'/media/{self.image_url}'

    class Meta:
        app_label = 'products'
