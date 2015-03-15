# -*- coding: utf-8 -*-
from django.db import models
from django.utils.encoding import smart_unicode
from zeltlager_registration.models import Participant
from zeltlager_registration.models import ZeltlagerDurchgang


class Booking(models.Model):
    number = models.IntegerField()
    participant = models.ForeignKey(Participant, blank=False, default=None)
    event = models.ForeignKey(ZeltlagerDurchgang, blank=False, default=None)
    comment = models.CharField(max_length=500, blank=True)
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
    