# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-07 08:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_song_is_favourite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='is_favourite',
        ),
    ]
