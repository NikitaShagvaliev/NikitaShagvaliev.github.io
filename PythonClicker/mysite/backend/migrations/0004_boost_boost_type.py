# Generated by Django 3.2 on 2021-05-30 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_maincycle_autoclickpower'),
    ]

    operations = [
        migrations.AddField(
            model_name='boost',
            name='boost_type',
            field=models.IntegerField(default=1),
        ),
    ]
