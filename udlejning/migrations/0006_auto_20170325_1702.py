# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-03-25 17:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('udlejning', '0005_remove_boardMemberInCharge_fields'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='udlejning',
            options={'ordering': ('dateFrom',)},
        ),
        migrations.AlterModelOptions(
            name='udlejninggrill',
            options={'ordering': ('dateFrom',)},
        ),
    ]
