# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-12-03 12:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galery', '0006_photo_miniture_big_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='height_miniature',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='image_miniature',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='width_miniature',
        ),
    ]
