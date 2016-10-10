# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import json


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_video', '0004_migrate_to_attributes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videoplayer',
            name='auto_hide',
        ),
        migrations.RemoveField(
            model_name='videoplayer',
            name='auto_play',
        ),
        migrations.RemoveField(
            model_name='videoplayer',
            name='bgcolor',
        ),
        migrations.RemoveField(
            model_name='videoplayer',
            name='buttonhighlightcolor',
        ),
        migrations.RemoveField(
            model_name='videoplayer',
            name='buttonoutcolor',
        ),
        migrations.RemoveField(
            model_name='videoplayer',
            name='buttonovercolor',
        ),
        migrations.RemoveField(
            model_name='videoplayer',
            name='fullscreen',
        ),
        migrations.RemoveField(
            model_name='videoplayer',
            name='height',
        ),
        migrations.RemoveField(
            model_name='videoplayer',
            name='loadingbarcolor',
        ),
        migrations.RemoveField(
            model_name='videoplayer',
            name='loop',
        ),
        migrations.RemoveField(
            model_name='videoplayer',
            name='seekbarbgcolor',
        ),
        migrations.RemoveField(
            model_name='videoplayer',
            name='seekbarcolor',
        ),
        migrations.RemoveField(
            model_name='videoplayer',
            name='textcolor',
        ),
        migrations.RemoveField(
            model_name='videoplayer',
            name='width',
        ),
    ]
