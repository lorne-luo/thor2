# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-19 01:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0015_auto_20171221_1334'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='alias',
            field=models.CharField(blank=True, max_length=255, verbose_name='alias'),
        ),
    ]