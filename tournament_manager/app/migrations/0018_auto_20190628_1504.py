# Generated by Django 2.2.2 on 2019-06-28 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_auto_20190628_0219'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='match',
            options={'verbose_name_plural': 'matches'},
        ),
        migrations.AlterField(
            model_name='match',
            name='time',
            field=models.TimeField(),
        ),
    ]