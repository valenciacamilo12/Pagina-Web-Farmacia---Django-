# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-08-13 00:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0012_auto_20190812_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='producto_imagen',
            field=models.FileField(default='productos/product_01.png', upload_to='productos'),
        ),
    ]