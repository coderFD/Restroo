# Generated by Django 4.0.5 on 2022-07-03 08:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0012_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='food_name',
        ),
    ]
