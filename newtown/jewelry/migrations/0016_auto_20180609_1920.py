# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-06-09 19:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jewelry', '0015_auto_20180609_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactlense',
            name='color',
            field=models.CharField(choices=[('Purple', 'PURPLE'), ('Blue', 'BLUE'), ('Green', 'GREEN'), ('Yellow', 'YELLOW'), ('Orange', 'ORANGE'), ('Red', 'RED')], default='Red', max_length=50, verbose_name='Color'),
        ),
    ]
