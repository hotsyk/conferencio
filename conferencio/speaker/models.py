# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

from postgres.fields import json_field

from event.models import Event
from users.models import User


class Speaker(models.Model):
    """
    Model to keep speakers data
    """
    user = models.ForeignKey(User)
    data = json_field.JSONField(default={})
    talks = models.ManyToManyField(Event, through='EventTalks')

    def __unicode__(self):
        return "{0} {1}".format(self.user.first_name, self.user.last_name)


class EventTalks(models.Model):
    """
    Link speakers to event with talk
    """
    event = models.ForeignKey(Event)
    speaker = models.ForeignKey(Speaker)
    title = models.CharField(_('Title of the talk'), max_length=1024)
    data = json_field.JSONField(default={})

    def __unicode__(self):
        return self.title
