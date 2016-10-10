# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import json


def migrate_to_attributes(apps, schema_editor):
    VideoPlayer = apps.get_model('djangocms_video', 'VideoPlayer')
    attrs = {}

    mapping = {
        'width': 'width',
        'height': 'height',
        'data-auto_play': 'auto_play',
        'data-auto_hide': 'auto_hide',
        'data-fullscreen': 'fullscreen',
        'data-loop': 'loop',
        'data-bgcolor': 'bgcolor',
        'data-textcolor': 'textcolor',
        'data-seekbarcolor': 'seekbarcolor',
        'data-seekbarbgcolor': 'seekbarbgcolor',
        'data-loadingbarcolor': 'loadingbarcolor',
        'data-buttonovercolor': 'buttonovercolor',
        'data-buttonhighlightcolor': 'buttonhighlightcolor',
    }

    for plugin in VideoPlayer.objects.all():
        for new, old in mapping.items():
            attrs[new] = str(getattr(plugin, old)).strip()
        # needs to be stored as dict to the database
        plugin.attributes = attrs
        plugin.save()


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_video', '0003_field_adaptions'),
    ]

    operations = [
        migrations.RunPython(migrate_to_attributes),
    ]
