# Generated by Django 4.0.5 on 2022-06-30 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_specialdish_order_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='date_time',
        ),
    ]