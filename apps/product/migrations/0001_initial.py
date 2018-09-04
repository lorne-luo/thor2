# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-09-04 11:04
from __future__ import unicode_literals

import apps.product.models
import core.django.models
import core.django.storage
from django.db import migrations, models
import django.db.models.deletion
import stdimage.models
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('member', '0001_initial'),
        ('store', '0001_initial'),
        ('taggit', '0002_auto_20150616_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_en', models.CharField(max_length=128, unique=True, verbose_name='name_en')),
                ('name_cn', models.CharField(blank=True, max_length=128, verbose_name='name_cn')),
                ('short_name', models.CharField(blank=True, max_length=128, verbose_name='Abbr')),
                ('remarks', models.CharField(blank=True, max_length=254, verbose_name='remarks')),
            ],
            options={
                'verbose_name': 'Brand',
                'verbose_name_plural': 'Brand',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=32, verbose_name='code')),
                ('name_en', models.CharField(blank=True, max_length=128, verbose_name='name_en')),
                ('name_cn', models.CharField(blank=True, max_length=128, verbose_name='name_cn')),
                ('brand_en', models.CharField(blank=True, max_length=128, verbose_name='brand_en')),
                ('brand_cn', models.CharField(blank=True, max_length=128, verbose_name='brand_cn')),
                ('alias', models.CharField(blank=True, max_length=255, verbose_name='alias')),
                ('country', models.CharField(blank=True, choices=[('AU', '澳洲'), ('US', '北美'), ('EU', '澳洲'), ('GB', '英国'), ('JP', '日本'), ('KR', '韩国'), ('TW', '台湾'), ('SEA', '东南亚')], default='AU', max_length=128, verbose_name='country')),
                ('pinyin', models.TextField(blank=True, max_length=512, verbose_name='pinyin')),
                ('pic', stdimage.models.StdImageField(blank=True, null=True, storage=core.django.storage.OverwriteStorage(), upload_to=apps.product.models.get_product_pic_path, verbose_name='picture')),
                ('spec', models.CharField(blank=True, max_length=128, verbose_name='spec')),
                ('weight', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='weight')),
                ('sold_count', models.IntegerField(default=0, verbose_name='Sold Count')),
                ('last_sell_price', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='last sell price')),
                ('avg_sell_price', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='avg sell price')),
                ('min_sell_price', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='min sell price')),
                ('max_sell_price', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='max sell price')),
                ('avg_cost', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='avg cost')),
                ('min_cost', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='min cost')),
                ('max_cost', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='max cost')),
                ('safe_sell_price', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='safe sell price')),
                ('tb_url', models.URLField(blank=True, null=True, verbose_name='TB URL')),
                ('wd_url', models.URLField(blank=True, null=True, verbose_name='WD URL')),
                ('wx_url', models.URLField(blank=True, null=True, verbose_name='WX URL')),
                ('uuid', models.CharField(blank=True, max_length=36, null=True, unique=True)),
                ('summary', models.TextField(blank=True, null=True, verbose_name='summary')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('is_active', models.BooleanField(default=True, verbose_name='is active')),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.Brand', verbose_name='brand')),
                ('page', models.ManyToManyField(blank=True, to='store.Page', verbose_name='page')),
                ('seller', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='member.Seller')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Product',
            },
            bases=(core.django.models.ResizeUploadedImageModelMixin, core.django.models.PinYinFieldModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='CustomProduct',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('product.product',),
        ),
        migrations.CreateModel(
            name='DefaultProduct',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('product.product',),
        ),
    ]
