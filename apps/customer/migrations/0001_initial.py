# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-09-04 11:04
from __future__ import unicode_literals

import apps.customer.models
import core.auth_user.models
import core.django.models
import core.django.storage
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('member', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='name')),
                ('pinyin', models.TextField(blank=True, max_length=512, verbose_name='pinyin')),
                ('mobile', models.CharField(blank=True, max_length=15, null=True, verbose_name='mobile number')),
                ('address', models.CharField(max_length=100, verbose_name='address')),
                ('id_number', models.CharField(blank=True, max_length=20, null=True, verbose_name='ID number')),
                ('id_photo_front', stdimage.models.StdImageField(blank=True, null=True, storage=core.django.storage.OverwriteStorage(), upload_to=apps.customer.models.get_id_photo_front_path, verbose_name='ID Front')),
                ('id_photo_back', stdimage.models.StdImageField(blank=True, null=True, storage=core.django.storage.OverwriteStorage(), upload_to=apps.customer.models.get_id_photo_back_path, verbose_name='ID Back')),
            ],
            options={
                'verbose_name': 'Address',
                'verbose_name_plural': 'Address',
            },
            bases=(core.django.models.ResizeUploadedImageModelMixin, core.django.models.PinYinFieldModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='姓名')),
                ('remark', models.CharField(blank=True, max_length=255, verbose_name='备注')),
                ('pinyin', models.TextField(blank=True, max_length=512, verbose_name='pinyin')),
                ('email', models.EmailField(blank=True, max_length=255, verbose_name='Email')),
                ('mobile', models.CharField(blank=True, max_length=15, verbose_name='手机')),
                ('order_count', models.PositiveIntegerField(blank=True, default=0, verbose_name='订单数')),
                ('last_order_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Last order time')),
                ('auth_user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer', to=settings.AUTH_USER_MODEL)),
                ('primary_address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='primary_address', to='customer.Address', verbose_name='默认地址')),
                ('seller', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='member.Seller', verbose_name='seller')),
            ],
            options={
                'verbose_name': 'Customer',
                'verbose_name_plural': 'Customer',
            },
            bases=(core.django.models.PinYinFieldModelMixin, core.auth_user.models.UserProfileMixin, models.Model),
        ),
        migrations.CreateModel(
            name='InterestTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='name')),
                ('remarks', models.CharField(blank=True, max_length=254, null=True, verbose_name='remarks')),
            ],
            options={
                'verbose_name': 'InterestTag',
                'verbose_name_plural': 'InterestTags',
            },
        ),
        migrations.AddField(
            model_name='customer',
            name='tags',
            field=models.ManyToManyField(blank=True, to='customer.InterestTag', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='address',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.Customer', verbose_name='customer'),
        ),
    ]
