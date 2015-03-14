# -*- coding: utf-8 -*-
from django.db import models
from django.utils.encoding import smart_unicode
from zeltlager_registration.models import Participant
from zeltlager_registration.models import ZeltlagerDurchgang

TRANSPORTATION_CHOICES = (('KFZ_Eigen', 'Eigenes KFZ'),
    ('KFZ_mitfahrt', 'Mitfahrer'),
    ('BusSMH', 'Bus ab SMH'),
    ('BusFS', 'Bus ab FS'),
    ('Bahn', 'Bahn'),
    ('Flugzeug', 'Flugzeug'),
    ('zuFuss', 'zu Fuss'),
    ('andere', 'andere'),
    ('keine', 'keine'))


class Booking(models.Model):
    number = models.IntegerField()
    participant = models.ForeignKey(Participant, blank=False, default=None)
    event = models.ForeignKey(ZeltlagerDurchgang, blank=False, default=None)
    arrival = models.DateTimeField()
    departure = models.DateTimeField()
    comment = models.CharField(max_length=500, blank=True)
    transportationBegin = models.CharField(max_length=20, blank=False)
    transportationBeginMethod = models.CharField(max_length=20, choices=TRANSPORTATION_CHOICES, default='keine')
    transportationEnd = models.CharField(max_length=20, blank=False)
    transportationEndMethod = models.CharField(max_length=20, choices=TRANSPORTATION_CHOICES, default='keine')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    hasPaid = models.BooleanField(default=False)
    isReduced = models.BooleanField(default=False)
    familyMembers = models.IntegerField()
    bookingDate = models.DateTimeField()
    
    class Meta:
        app_label = 'zeltlager_management'
        verbose_name = 'Buchung'
        verbose_name_plural = 'Buchungen'
        
    def __unicode__(self):
        return smart_unicode(str(self.number) + ", " + self.participant.name)
    