# Generated by Django 3.2 on 2021-05-30 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20210517_2153'),
    ]

    operations = [
        migrations.AddField(
            model_name='maincycle',
            name='autoClickPower',
            field=models.IntegerField(default=0),
        ),
    ]
