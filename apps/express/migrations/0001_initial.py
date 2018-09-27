# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-09-10 23:43
from __future__ import unicode_literals

import core.django.db
import core.django.models
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExpressCarrier',
            fields=[
                ('id', models.IntegerField()),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('schema_name', models.CharField(blank=True, default=core.django.db.get_schema_name, max_length=32)),
                ('name_cn', models.CharField(help_text='中文名称', max_length=255, verbose_name='中文名称')),
                ('name_en', models.CharField(blank=True, help_text='英文名称', max_length=255, verbose_name='英文名称')),
                ('pinyin', models.TextField(blank=True, max_length=512, verbose_name='pinyin')),
                ('website', models.URLField(blank=True, help_text='官方网站地址', verbose_name='官网地址')),
                ('search_url', models.URLField(blank=True, help_text='查询网页地址', verbose_name='查询网址')),
                ('post_search_url', models.URLField(blank=True, help_text='查询提交网址', verbose_name='查询提交网址')),
                ('id_upload_url', models.URLField(blank=True, help_text='证件上传地址', verbose_name='证件上传地址')),
                ('rate', models.DecimalField(blank=True, decimal_places=2, help_text='每公斤费率', max_digits=6, null=True, verbose_name='费率')),
                ('is_default', models.BooleanField(default=False, help_text='是否默认', verbose_name='默认')),
                ('track_id_regex', models.CharField(blank=True, help_text='订单号正则表达式', max_length=512, verbose_name='单号正则')),
                ('domain', models.CharField(blank=True, max_length=512, verbose_name='domain')),
            ],
            options={
                'abstract': False,
            },
            bases=(core.django.models.PinYinFieldModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='ExpressOrder',
            fields=[
                ('id', models.IntegerField()),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('schema_name', models.CharField(blank=True, default=core.django.db.get_schema_name, max_length=32)),
                ('track_id', models.CharField(help_text='运单号', max_length=30, verbose_name='Track ID')),
                ('is_delivered', models.BooleanField(default=False, verbose_name='is delivered')),
                ('last_track', models.CharField(blank=True, max_length=512, null=True, verbose_name='last track')),
                ('fee', models.DecimalField(decimal_places=2, default=0, help_text='运费', max_digits=8, verbose_name='Shipping Fee')),
                ('weight', models.DecimalField(blank=True, decimal_places=2, help_text='重量', max_digits=8, null=True, verbose_name='Weight')),
                ('id_upload', models.BooleanField(default=False, verbose_name='ID uploaded')),
                ('remarks', models.CharField(blank=True, max_length=128, null=True, verbose_name='Remarks')),
                ('delivery_sms_sent', models.BooleanField(default=False, verbose_name='delivery sms')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='Create Time')),
                ('delivered_time', models.DateTimeField(blank=True, null=True, verbose_name='寄达时间')),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='customer.Address', verbose_name='address')),
                ('carrier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='express.ExpressCarrier', verbose_name='carrier')),
            ],
            options={
                'verbose_name': 'Express Order',
                'verbose_name_plural': 'Express Order',
            },
        ),
    ]