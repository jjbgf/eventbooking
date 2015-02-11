from django.contrib import admin
from zeltlager_registration.models import ZeltlagerDurchgang, Participant,\
    Jugendgruppe, Address

admin.site.register(ZeltlagerDurchgang)
admin.site.register(Participant)
admin.site.register(Jugendgruppe)
admin.site.register(Address)