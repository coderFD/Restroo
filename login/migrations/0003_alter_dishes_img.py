# Generated by Django 4.0.5 on 2022-06-27 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_rename_dish_desc_dishes_desc_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dishes',
            name='img',
            field=models.ImageField(upload_to='pics'),
        ),
    ]
