# Generated by Django 4.0.5 on 2022-07-03 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0011_dishes_code_menu_code_specialdish_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('food_name', models.CharField(max_length=20)),
                ('code', models.IntegerField()),
                ('img', models.ImageField(upload_to='pics')),
            ],
        ),
    ]
