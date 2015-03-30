
from django.contrib.auth import get_user_model
import factory

from .. import models


class UserFactory(factory.Factory):
    class Meta:
        model = get_user_model()

    first_name = 'John'
    last_name = 'Doe'
    email = 'test@test.com'


class SpeakerFactory(factory.Factory):

    class Meta:
        model = models.Speaker

    data = {'bio': 'Some bio string here'}
    user = UserFactory.create()
