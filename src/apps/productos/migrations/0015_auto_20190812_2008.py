# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-08-13 01:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0014_auto_20190812_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='producto_imagen',
            field=models.ImageField(default='productos/product_01.png', upload_to='media/productos'),
        ),
    ]