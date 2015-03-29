# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import postgres.fields
import decimal
import django.core.serializers.json
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0005_auto_20150315_1026'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EventTalks',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=1024, verbose_name='Title of the talk')),
                ('data', postgres.fields.JSONField(default={}, encode_kwargs={'cls': django.core.serializers.json.DjangoJSONEncoder}, decode_kwargs={'parse_float': decimal.Decimal})),
                ('event', models.ForeignKey(to='event.Event')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data', postgres.fields.JSONField(default={}, encode_kwargs={'cls': django.core.serializers.json.DjangoJSONEncoder}, decode_kwargs={'parse_float': decimal.Decimal})),
                ('talks', models.ManyToManyField(to='event.Event', through='speaker.EventTalks')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='eventtalks',
            name='speaker',
            field=models.ForeignKey(to='speaker.Speaker'),
            preserve_default=True,
        ),
    ]
