# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-08-12 20:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0009_auto_20190812_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='producto_imagen',
            field=models.ImageField(default='img/product_01.png', upload_to='static/img'),
        ),
    ]