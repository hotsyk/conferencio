# -*- coding: utf-8 -*-
import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _

from postgres.fields import json_field

from users.models import User


class EventSeries(models.Model):
    """
    Every event series should be separated as could have different organizers
    """

    admin = models.ForeignKey(User, related_name='eventseries_owner')
    domain = models.CharField(_('domain of site'), max_length=1024)
    title = models.CharField(_('title of event series'), max_length=255)
    moderators = models.ManyToManyField(User,
                                        related_name='eventseries_moderator')

    def __unicode__(self):
        return self.title


class EventKind(models.Model):
    """
    Generalized model to keep types of events:
    conference/seminar/meetup/etc
    """

    title = models.CharField(max_length=255)

    def __unicode__(self):
        return self.title


class EventCountry(models.Model):
    title = models.CharField(max_length=255)

    def __unicode__(self):
        return self.title


class EventCity(models.Model):
    country = models.ForeignKey(EventCountry)
    title = models.CharField(max_length=255)

    def __unicode__(self):
        return self.title


class Event(models.Model):
    """
    Separate events
    """
    city = models.ForeignKey(EventCity, blank=True, null=True)
    context = json_field.JSONField(default={})
    kind = models.ForeignKey(EventKind)
    ts_create = models.DateTimeField(default=datetime.datetime.now)
    ts_start = models.DateTimeField(null=True)
    ts_end = models.DateTimeField(null=True)
    registered_users = models.ManyToManyField(
        User,
        related_name='event_registrants')
    organizers = models.ManyToManyField(User, related_name='event_orgnizer')
    schedule = json_field.JSONField(default={})
    series = models.ForeignKey(EventSeries)
    venue = json_field.JSONField(default={})
    title = models.CharField(_('title of event'), max_length=1024)

    def __unicode__(self):
        return self.title
