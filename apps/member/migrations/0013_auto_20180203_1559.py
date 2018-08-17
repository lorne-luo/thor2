# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-03 04:59


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0012_seller_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='primary_currency',
            field=models.CharField(blank=True, choices=[('AUDCNH', '\u6fb3\u5143'), ('USDCNH', '\u7f8e\u5143'), ('NZDCNH', '\u7ebd\u5143'), ('EURCNH', '\u6b27\u5143'), ('GBPCNH', '\u82f1\u9551'), ('CADCNH', '\u52a0\u5143'), ('JPYCNH', '\u65e5\u5143')], default='AUDCNH', max_length=128, verbose_name='\u9996\u9009\u8d27\u5e01'),
        ),
        migrations.AlterField(
            model_name='seller',
            name='country',
            field=models.CharField(blank=True, choices=[('AU', '\u6fb3\u6d32'), ('US', '\u5317\u7f8e'), ('EU', '\u6fb3\u6d32'), ('G', '\u82f1\u56fd'), ('JP', '\u65e5\u672c'), ('KR', '\u97e9\u56fd'), ('TW', '\u53f0\u6e7e'), ('SEA', '\u4e1c\u5357\u4e9a')], default='AU', max_length=128, verbose_name='\u56fd\u5bb6'),
        ),
        migrations.AlterField(
            model_name='seller',
            name='name',
            field=models.CharField(blank=True, default='', max_length=30, verbose_name='\u59d3\u540d'),
            preserve_default=False,
        ),
    ]
