# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-06-13 18:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jewelry', '0019_display_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='display',
            name='image',
            field=models.ImageField(null=True, upload_to='display/', verbose_name='Image of Jewelry'),
        ),
    ]