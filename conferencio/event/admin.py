from django.contrib import admin

from .models import (
    Event,
    EventCity,
    EventCountry,
    EventKind,
    EventSeries,
)


admin.site.register(Event)
admin.site.register(EventCity)
admin.site.register(EventCountry)
admin.site.register(EventKind)
admin.site.register(EventSeries)
