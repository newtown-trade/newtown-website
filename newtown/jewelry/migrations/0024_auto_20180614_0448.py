# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-06-14 04:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jewelry', '0023_auto_20180614_0448'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='display',
            options={},
        ),
        migrations.AlterModelOptions(
            name='metal',
            options={'verbose_name': 'Earring, Nose Hook, Bracelet', 'verbose_name_plural': 'Earrings, Nose Hooks, Bracelets'},
        ),
    ]
