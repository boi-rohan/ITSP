# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-25 20:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avbl', '0004_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='court',
            name='image_src',
            field=models.CharField(default=b'', max_length=1000),
        ),
        migrations.AlterField(
            model_name='court',
            name='court_location',
            field=models.CharField(default=b'', max_length=1000),
        ),
    ]