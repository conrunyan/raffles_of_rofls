from django.contrib import admin
from raffle_backend.models import Participant, Session, Host, Winner

# Register your models here.
admin.site.register(Participant)
admin.site.register(Session)
admin.site.register(Host)
admin.site.register(Winner)
