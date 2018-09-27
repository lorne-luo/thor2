# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-09-18 11:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carrier_tracker', '0002_auto_20180907_0910'),
    ]

    operations = [
        migrations.AddField(
            model_name='carriertracker',
            name='item_index',
            field=models.IntegerField(blank=True, default=-1, verbose_name='item_index'),
        ),
        migrations.AddField(
            model_name='carriertracker',
            name='item_tag',
            field=models.CharField(blank=True, default='tr', max_length=255, verbose_name='item_tag'),
        ),
        migrations.AddField(
            model_name='carriertracker',
            name='list_class',
            field=models.CharField(blank=True, max_length=255, verbose_name='list_class'),
        ),
        migrations.AddField(
            model_name='carriertracker',
            name='list_id',
            field=models.CharField(blank=True, max_length=255, verbose_name='list_id'),
        ),
        migrations.AddField(
            model_name='carriertracker',
            name='list_tag',
            field=models.CharField(blank=True, default='table', max_length=255, verbose_name='list_tag'),
        ),
    ]