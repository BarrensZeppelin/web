# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-03-25 15:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='inStock',
            field=models.BooleanField(default=True),
        ),
    ]
