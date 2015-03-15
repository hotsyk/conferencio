import datetime

from django.contrib.auth import get_user_model
import factory

from .. import models


class UserFactory(factory.Factory):
    class Meta:
        model = get_user_model()

    first_name = 'John'
    last_name = 'Doe'
    email = 'test@test.com'


class EventCountryFactory(factory.Factory):
    class Meta:
        model = models.EventCountry

    title = 'Ukraine'


class EventCityFactory(factory.Factory):
    class Meta:
        model = models.EventCity

    title = 'Kyiv'
    country = EventCountryFactory.create()


class EventKindFactory(factory.Factory):
    class Meta:
        model = models.EventKind

    title = 'meetup'


class EventSeriesFactory(factory.Factory):
    class Meta:
        model = models.EventSeries

    admin = UserFactory.create()
    domain = 'my_meetup.com'
    title = 'My Meetup'
    #moderators = [UserFactory.create(), UserFactory.create()]


class EventFactory(factory.Factory):

    class Meta:
        model = models.Event

    city = EventCityFactory.create()
    context = {'some_context': 1}
    kind = EventKindFactory.create()
    ts_start = datetime.datetime.now() + datetime.timedelta(days=5)
    ts_end = ts_start + datetime.timedelta(days=7)
    schedule = {'Day 1': {'Stage 1': [{'9:00': "Registration"}]}}
    series = EventSeriesFactory.create()
    venue = {'title': 'My Venue', 'address': '234234'}
    title = 'My meetup #1'
    #registered_users = [UserFactory.create(), UserFactory.create()]
    #organizers = [UserFactory.create(), UserFactory.create()]
