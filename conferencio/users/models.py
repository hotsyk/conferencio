# -*- coding: utf-8 -*-
# Import the AbstractUser model
from django.contrib.auth.models import AbstractUser

# Import the basic Django ORM models library
from django.db import models

from django.utils.translation import ugettext_lazy as _

from postgres.fields import json_field


class User(AbstractUser):

    context = json_field.JSONField(default={})
    action_history = json_field.JSONField(default={})

    date_of_birth = models.DateField(
        _('date of birth of user'), null=True)

    def __unicode__(self):
        return self.username
