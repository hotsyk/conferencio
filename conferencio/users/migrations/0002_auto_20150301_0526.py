# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.serializers.json
import postgres.fields
import decimal


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='action_history',
            field=postgres.fields.JSONField(default={}, encode_kwargs={'cls': django.core.serializers.json.DjangoJSONEncoder}, decode_kwargs={'parse_float': decimal.Decimal}),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='context',
            field=postgres.fields.JSONField(default={}, encode_kwargs={'cls': django.core.serializers.json.DjangoJSONEncoder}, decode_kwargs={'parse_float': decimal.Decimal}),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='date_of_birth',
            field=models.DateField(null=True, verbose_name='date of birth of user'),
            preserve_default=True,
        ),
    ]
