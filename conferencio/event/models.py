from django.db import models


class EventsKind(models.Model):
    title = models.CharField(max_length=255)


class Event(models.Model):
    kind = models.ForeignKey(EventsKind)
