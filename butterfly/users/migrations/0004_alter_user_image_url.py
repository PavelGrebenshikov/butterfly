# Generated by Django 3.2.14 on 2022-07-22 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20220720_0825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image_url',
            field=models.ImageField(default='/static/images/profile.png', upload_to='users/avatars/', verbose_name='Image url'),
        ),
    ]