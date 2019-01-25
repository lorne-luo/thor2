# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-11-15 02:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carrier_tracker', '0004_auto_20181029_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carriertracker',
            name='alias',
            field=models.CharField(blank=True, max_length=255, verbose_name='别名'),
        ),
        migrations.AlterField(
            model_name='carriertracker',
            name='id_upload_url',
            field=models.URLField(blank=True, help_text='证件上传地址', max_length=1024, verbose_name='证件上传地址'),
        ),
        migrations.AlterField(
            model_name='carriertracker',
            name='item_index',
            field=models.IntegerField(blank=True, default=-1, verbose_name='顺序'),
        ),
        migrations.AlterField(
            model_name='carriertracker',
            name='post_search_url',
            field=models.URLField(blank=True, help_text='查询提交网址', max_length=1024, verbose_name='查询提交网址'),
        ),
        migrations.AlterField(
            model_name='carriertracker',
            name='search_url',
            field=models.URLField(blank=True, help_text='查询网页地址', max_length=1024, verbose_name='查询网址'),
        ),
        migrations.AlterField(
            model_name='carriertracker',
            name='selector',
            field=models.CharField(blank=True, default='table tr', max_length=255, verbose_name='CSS'),
        ),
        migrations.AlterField(
            model_name='carriertracker',
            name='website',
            field=models.URLField(blank=True, help_text='官方网站地址', max_length=255, verbose_name='官网地址'),
        ),
    ]