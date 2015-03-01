# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_auto_20150301_0626'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='title',
            field=models.CharField(default='Title', max_length=1024, verbose_name='title of event'),
            preserve_default=False,
        ),
    ]
