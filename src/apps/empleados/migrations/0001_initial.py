# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-08-09 17:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('cod_emp', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('nom_emp', models.CharField(max_length=30)),
                ('dir_emp', models.CharField(max_length=30)),
                ('cargo', models.CharField(max_length=30)),
                ('edad', models.IntegerField()),
                ('telefono', models.IntegerField()),
                ('celular', models.IntegerField()),
            ],
        ),
    ]
