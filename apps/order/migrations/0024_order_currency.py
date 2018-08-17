# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-03 05:34


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0023_orderproduct_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='currency',
            field=models.CharField(blank=True, choices=[('AUDCNH', '\u6fb3\u5143'), ('USDCNH', '\u7f8e\u5143'), ('NZDCNH', '\u7ebd\u5143'), ('EURCNH', '\u6b27\u5143'), ('GBPCNH', '\u82f1\u9551'), ('CADCNH', '\u52a0\u5143'), ('JPYCNH', '\u65e5\u5143')], max_length=128, verbose_name='\u8d27\u5e01'),
        ),
    ]
