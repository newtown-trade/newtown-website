# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-06-15 14:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jewelry', '0028_auto_20180615_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='display',
            name='name',
            field=models.CharField(default='name', max_length=50, verbose_name='Name of Display'),
        ),
    ]
