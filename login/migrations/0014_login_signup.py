# Generated by Django 4.0.5 on 2022-07-03 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0013_remove_cart_food_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=12)),
                ('c_pwd', models.CharField(max_length=12)),
            ],
        ),
    ]
