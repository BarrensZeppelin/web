# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-06-14 19:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_auto_20170325_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
