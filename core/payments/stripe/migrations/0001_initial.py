# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-11 01:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('djstripe', '0011_auto_20170808_0628'),
    ]

    operations = [
        migrations.CreateModel(
            name='StripeInvoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paid', models.BooleanField(default=False)),
                ('refunded', models.BooleanField(default=False)),
                ('status', models.CharField(blank=True, max_length=32)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('amount_refunded', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('description', models.TextField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('charge', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='djstripe.Charge')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='djstripe.Customer')),
            ],
        ),
    ]
