# Generated by Django 3.2.5 on 2022-09-25 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='latitude',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='event',
            name='longitude',
            field=models.FloatField(default=0.0),
        ),
    ]
