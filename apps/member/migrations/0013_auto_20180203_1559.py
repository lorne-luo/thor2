# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-03 04:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0012_seller_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='primary_currency',
            field=models.CharField(blank=True, choices=[(b'AUDCNH', '\u6fb3\u5143'), (b'USDCNH', '\u7f8e\u5143'), (b'NZDCNH', '\u7ebd\u5143'), (b'EURCNH', '\u6b27\u5143'), (b'GBPCNH', '\u82f1\u9551'), (b'CADCNH', '\u52a0\u5143'), (b'JPYCNH', '\u65e5\u5143')], default=b'AUDCNH', max_length=128, verbose_name='\u9996\u9009\u8d27\u5e01'),
        ),
        migrations.AlterField(
            model_name='seller',
            name='country',
            field=models.CharField(blank=True, choices=[(b'AU', '\u6fb3\u6d32'), (b'US', '\u5317\u7f8e'), (b'EU', '\u6fb3\u6d32'), (b'GB', '\u82f1\u56fd'), (b'JP', '\u65e5\u672c'), (b'KR', '\u97e9\u56fd'), (b'TW', '\u53f0\u6e7e'), (b'SEA', '\u4e1c\u5357\u4e9a')], default=b'AU', max_length=128, verbose_name='\u56fd\u5bb6'),
        ),
        migrations.AlterField(
            model_name='seller',
            name='name',
            field=models.CharField(blank=True, default='', max_length=30, verbose_name='\u59d3\u540d'),
            preserve_default=False,
        ),
    ]