# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-09-10 23:43
from __future__ import unicode_literals

import core.auth_user.models
import core.django.db
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MembershipOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_at', models.DateField(blank=True, null=True, verbose_name='membership start at')),
                ('end_at', models.DateField(blank=True, null=True, verbose_name='membership expire at')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name='membership payment')),
                ('create_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='create at')),
            ],
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.IntegerField()),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('schema_name', models.CharField(blank=True, default=core.django.db.get_schema_name, max_length=32)),
                ('tenant_id', models.CharField(blank=True, max_length=128, verbose_name='tenant_id')),
                ('name', models.CharField(blank=True, max_length=30, verbose_name='姓名')),
                ('country', models.CharField(blank=True, choices=[('AU', '澳洲'), ('US', '北美'), ('EU', '澳洲'), ('GB', '英国'), ('JP', '日本'), ('KR', '韩国'), ('TW', '台湾'), ('SEA', '东南亚')], default='AU', max_length=128, verbose_name='国家')),
                ('expire_at', models.DateField(blank=True, null=True, verbose_name='member expire at')),
                ('start_at', models.DateField(blank=True, null=True, verbose_name='member start at')),
                ('primary_currency', models.CharField(blank=True, choices=[('AUDCNH', '澳元'), ('USDCNH', '美元'), ('NZDCNH', '纽元'), ('EURCNH', '欧元'), ('GBPCNH', '英镑'), ('CADCNH', '加元'), ('JPYCNH', '日元')], default='AUDCNH', max_length=128, verbose_name='首选货币')),
                ('create_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='create at')),
                ('auth_user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='seller', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['id'],
            },
            bases=(core.auth_user.models.UserProfileMixin, models.Model),
        ),
        migrations.AddField(
            model_name='membershiporder',
            name='seller',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='member.Seller'),
        ),
    ]
