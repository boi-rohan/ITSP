# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-26 03:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('avbl', '0008_auto_20170526_0844'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datetimevalue',
            name='date_time',
        ),
    ]