# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-09-06 05:08
from __future__ import unicode_literals

import core.django.models
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='schema_name',
            field=models.CharField(blank=True, default=core.django.models.get_schema_name, max_length=32),
        ),
        migrations.AddField(
            model_name='store',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
