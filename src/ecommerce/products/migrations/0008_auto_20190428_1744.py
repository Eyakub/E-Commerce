# Generated by Django 2.2 on 2019-04-28 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20190428_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, default='abc', null=True, unique=True),
        ),
    ]