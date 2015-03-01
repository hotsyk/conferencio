# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='city',
            field=models.ForeignKey(blank=True, to='event.EventCity', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='eventcity',
            name='country',
            field=models.ForeignKey(default=None, to='event.EventCountry'),
            preserve_default=False,
        ),
    ]
