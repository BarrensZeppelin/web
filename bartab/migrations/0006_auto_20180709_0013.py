# Generated by Django 2.0.6 on 2018-07-08 22:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bartab', '0005_auto_20180708_2342'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bartabsnapshot',
            options={'ordering': ('bartender_shift__is_null', '-bartender_shift__start_datetime')},
        ),
    ]