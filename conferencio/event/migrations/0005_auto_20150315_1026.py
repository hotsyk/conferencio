# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0004_auto_20150314_1301'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eventseries',
            old_name='users',
            new_name='moderators',
        ),
    ]
