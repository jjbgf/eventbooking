from django.db import models
from zeltlager_registration.models import Participant, ZeltlagerDurchgang

#define enum in python 2.7
def enum(**enums):
    return type('Enum', (), enums)

transportation = enum(KFZ_Eigen = 'KFZ_Eigen',
    KFZ_mitfahrt = 'KFZ_mitfahrt',
    BusSMH = 'BusSMH',
    BusFS = 'BusFS',
    Bahn = 'Bahn',
    Flugzeug = 'Flugzeug',
    zuFuss = 'zuFuss',
    andere = 'andere',
    keine = 'keine')

gender = enum(WOMAN = 0, MAN = 1)

function = enum(Jugendleiter = 'Jugendleiter', Prediger = 'Prediger', Hauptjugendleiter = 'Hauptjugendleiter')
    

class Booking(models.Model):
    number = models.IntegerField()
    participant = models.ForeignKey(Participant, blank=True, default=None)
    event = models.ForeignKey(ZeltlagerDurchgang, blank=True, default=None)
    arrival = models.DateTimeField()
    departure = models.DateTimeField()
    comment = models.CharField(max_length=500, blank=True)
    transportationBegin = models.CharField(max_length=20, blank=False)
    transportationEnd = models.CharField(max_length=20, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    hasPaid = models.BooleanField(default=False)
    isReduced = models.BooleanField(default=False)
    familyMembers = models.IntegerField()
    bookingDate = models.DateTimeField()
    
    
    