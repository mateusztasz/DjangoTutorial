# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-10 18:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_song_is_favourite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_logo',
            field=models.FileField(upload_to=''),
        ),
    ]
