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



admin.site.register(EventCity)
admin.site.register(EventCountry)
admin.site.register(EventKind)
admin.site.register(EventSeries)
