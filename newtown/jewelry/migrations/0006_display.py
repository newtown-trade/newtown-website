# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-29 03:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jewelry', '0005_auto_20180522_2223'),
    ]

    operations = [
        migrations.CreateModel(
            name='Display',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jewelryset', models.ManyToManyField(to='jewelry.Metal')),
            ],
        ),
    ]
