# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-06-14 20:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('jewelry', '0025_auto_20180614_0453'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactlense',
            name='timestampe',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='display',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='metal',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
