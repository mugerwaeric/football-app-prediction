# Generated by Django 2.2.2 on 2019-06-28 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_auto_20190628_1504'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='started',
            field=models.BooleanField(default=False),
        ),
    ]
