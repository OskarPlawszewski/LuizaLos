# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-11-13 12:42
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20161113_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 13, 12, 42, 19, 430968, tzinfo=utc)),
        ),
    ]