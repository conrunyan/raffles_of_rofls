from django.contrib import admin

# Register your models here.

from .models import Participant, RaffleSession

admin.site.register(Participant)
admin.site.register(RaffleSession)