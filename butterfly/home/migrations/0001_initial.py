# Generated by Django 3.2.14 on 2022-07-25 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Name of category')),
            ],
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name of subcategory')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Product name')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Price')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='Last modifying')),
                ('visible', models.BooleanField(default=True, verbose_name='Is visible')),
                ('image_url', models.ImageField(default='/static/images/product.png', upload_to='products/photos/', verbose_name='Image url')),
                ('category', models.ManyToManyField(to='home.Category')),
                ('subcategory', models.ManyToManyField(to='home.Subcategory')),
            ],
        ),
    ]
