# Generated by Django 2.0.6 on 2018-07-09 23:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('udlejning', '0009_auto_20180710_0127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='udlejningapplication',
            name='billSendTo',
        ),
    ]