#import datetime

from django.test import TestCase

from .factories import SpeakerFactory


class TestSpeaker(TestCase):

    def test_setup_event(self):
        speaker = SpeakerFactory.create()
        self.assertEqual(speaker.data['bio'], 'Some bio string here')
