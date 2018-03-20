# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-20 00:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jewelry', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jewelry',
            name='jewelry_type',
            field=models.CharField(choices=[('GLD', 'Gold'), ('SLVR', 'Silver'), ('BRNZ', 'Bronze'), ('STL', 'Steel')], default='GLD', max_length=4),
        ),
    ]
