from django.contrib import admin

from .models import (
    Event,
    EventCity,
    EventCountry,
    EventKind,
    EventSeries,
)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    date_hierarchy = 'ts_start'


@admin.register(EventCity)
class EventCityAdmin(admin.ModelAdmin):
    pass


@admin.register(EventCountry)
class EventCountryAdmin(admin.ModelAdmin):
    pass


@admin.register(EventKind)
class EventKindAdmin(admin.ModelAdmin):
    pass


@admin.register(EventSeries)
class EventSeriesAdmin(admin.ModelAdmin):
    pass
