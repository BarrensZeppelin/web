# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-03-25 16:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bartenders', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bartender',
            options={'ordering': ('name',)},
        ),
    ]