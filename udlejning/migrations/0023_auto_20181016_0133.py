# Generated by Django 2.1.2 on 2018-10-15 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('udlejning', '0022_auto_20180726_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='udlejning',
            name='actualConsummation',
            field=models.TextField(blank=True, max_length=140, verbose_name='Faktisk forbrug'),
        ),
        migrations.AlterField(
            model_name='udlejning',
            name='bartendersInCharge',
            field=models.ManyToManyField(blank=True, to='bartenders.Bartender', verbose_name='Ansvarlige'),
        ),
        migrations.AlterField(
            model_name='udlejning',
            name='billSendTo',
            field=models.CharField(max_length=140, verbose_name='Send regning til'),
        ),
    ]