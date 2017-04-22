# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-22 01:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='owner',
        ),
        migrations.AlterField(
            model_name='cart',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
