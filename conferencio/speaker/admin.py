from django.contrib import admin

from .models import Proposal, Speaker


@admin.register(Speaker)
class SpeakerAdmin(admin.ModelAdmin):
    pass


@admin.register(Proposal)
class ProposalAdmin(admin.ModelAdmin):
    pass
