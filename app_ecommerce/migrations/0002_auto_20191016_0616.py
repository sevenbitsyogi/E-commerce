# Generated by Django 2.2.6 on 2019-10-16 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_ecommerce', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='', max_length=150, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='', max_length=100),
        ),
    ]
