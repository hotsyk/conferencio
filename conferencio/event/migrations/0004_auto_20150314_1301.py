# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_event_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='ts_create',
            field=models.DateTimeField(default=datetime.datetime.now),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='ts_end',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='ts_start',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
    ]
