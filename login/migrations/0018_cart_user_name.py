# Generated by Django 4.0.5 on 2022-07-04 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0017_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='user_name',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
    ]
