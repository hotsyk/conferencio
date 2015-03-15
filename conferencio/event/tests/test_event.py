#import datetime

from django.test import TestCase

#from .. import models
from .factories import EventFactory


class TestEvent(TestCase):

    def test_setup_event(self):
        event = EventFactory.create()
        self.assertEqual(event.city.title, 'Kyiv')
