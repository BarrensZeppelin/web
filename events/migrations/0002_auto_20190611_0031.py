# Generated by Django 2.2.2 on 2019-06-10 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventresponse',
            name='respo',
        ),
        migrations.AddField(
            model_name='eventresponse',
            name='choices',
            field=models.ManyToManyField(to='events.EventChoiceOption'),
        ),
        migrations.DeleteModel(
            name='EventChoiceResponse',
        ),
    ]
