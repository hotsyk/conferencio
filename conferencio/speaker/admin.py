from django.contrib import admin

from .models import Speaker


@admin.register(Speaker)
class SpeakerAdmin(admin.ModelAdmin):
    pass
