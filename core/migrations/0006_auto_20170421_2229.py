# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-22 01:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20170421_2210'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='cart',
            name='cod',
            field=models.PositiveIntegerField(),
        ),
    ]
