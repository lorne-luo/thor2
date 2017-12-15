# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-11 22:39
from __future__ import unicode_literals

from django.db import migrations, models
from django.db.models import F, Avg, Sum, Min, Max


def forwards_func(apps, schema_editor):
    Product = apps.get_model("product", "product")
    OrderProduct = apps.get_model("order", "orderproduct")
    for p in Product.objects.all():
        product_sales = OrderProduct.objects.filter(product=p).order_by('-id')
        if product_sales.count():
            data = product_sales.aggregate(sold_count=Sum(F('amount')),
                                           avg_sell_price=Avg(F('sell_price_rmb')),
                                           min_sell_price=Min(F('sell_price_rmb')),
                                           max_sell_price=Max(F('sell_price_rmb')),
                                           avg_cost=Avg(F('cost_price_aud')),
                                           min_cost=Min(F('cost_price_aud')),
                                           max_cost=Max(F('cost_price_aud')))
            p.last_sell_price = product_sales.first().sell_price_rmb
            p.avg_sell_price = data.get('avg_sell_price') or None
            p.min_sell_price = data.get('min_sell_price') or None
            p.max_sell_price = data.get('max_sell_price') or None
            p.avg_cost = data.get('avg_cost') or None
            p.min_cost = data.get('min_cost') or None
            p.max_cost = data.get('max_cost') or None
            p.sold_count = data.get('sold_count') or 0
            p.save()


def backwarad_func(apps, schema_editor):
    print "nothing to migrate"


class Migration(migrations.Migration):
    dependencies = [
        ('product', '0013_auto_20171212_0916'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='spec1',
            new_name='spec',
        ),
        migrations.RemoveField(
            model_name='product',
            name='spec2',
        ),
        migrations.RemoveField(
            model_name='product',
            name='spec3',
        ),
        migrations.RemoveField(
            model_name='product',
            name='bargain_price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='full_price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='normal_price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='sell_price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='state',
        ),
        migrations.AddField(
            model_name='product',
            name='avg_sell_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True,
                                      verbose_name='avg sell price'),
        ),
        migrations.AddField(
            model_name='product',
            name='last_sell_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True,
                                      verbose_name='last sell price'),
        ),
        migrations.AddField(
            model_name='product',
            name='max_sell_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True,
                                      verbose_name='max sell price'),
        ),
        migrations.AddField(
            model_name='product',
            name='min_sell_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True,
                                      verbose_name='min sell price'),
        ),
        migrations.AddField(
            model_name='product',
            name='avg_cost',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True,
                                      verbose_name='avg cost'),
        ),
        migrations.AddField(
            model_name='product',
            name='max_cost',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True,
                                      verbose_name='max cost'),
        ),
        migrations.AddField(
            model_name='product',
            name='min_cost',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True,
                                      verbose_name='min cost'),
        ),
        migrations.AddField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='is active'),
        ),
        migrations.AlterField(
            model_name='product',
            name='spec',
            field=models.CharField(blank=True, default='', max_length=128, verbose_name='spec'),
            preserve_default=False,
        ),
        migrations.RunPython(forwards_func, backwarad_func),
    ]