# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.serializers.json
from django.conf import settings
import decimal
import postgres.fields


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0005_auto_20150315_1026'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('speaker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proposal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=1024, verbose_name='Title of the talk')),
                ('data', postgres.fields.JSONField(default={}, encode_kwargs={'cls': django.core.serializers.json.DjangoJSONEncoder}, decode_kwargs={'parse_float': decimal.Decimal})),
                ('event', models.ForeignKey(to='event.Event')),
                ('proposer', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
