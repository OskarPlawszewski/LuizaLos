# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-11-30 21:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galery', '0003_auto_20161130_2235'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='image_miniature',
            field=models.ImageField(height_field='height', null=True, upload_to='', width_field='width'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(height_field='height', upload_to='', width_field='width'),
        ),
    ]