# Generated by Django 2.2.2 on 2020-01-13 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bartenders', '0039_bartenderapplication_tshirt_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='bartenderapplication',
            name='study',
            field=models.CharField(default='?', max_length=50, verbose_name='Studie'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bartenderapplication',
            name='study_year',
            field=models.IntegerField(default=0, verbose_name='Årgang'),
            preserve_default=False,
        ),
    ]
