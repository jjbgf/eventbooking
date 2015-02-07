from django.db import models
from zeltlager_registration.models import Participant

# Create your models here.

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

# TODO: Insert is as initial content to db
youthgroup = enum(BadenBaden = 'BadenBaden',
    BerlinKaulsdorf = 'BerlinKaulsdorf',
    BerlinSMH = 'BerlinSMH',
    BREMEN = 'BREMEN',
    Dortmund = 'Dortmund',
    Dresden = 'Dresden',
    Duesseldorf = 'Duesseldorf',
    FrankfurtOder = 'FrankfurtOder',
    Fuerstenwalde = 'Fuerstenwalde',
    Goessweinstein = 'Goessweinstein',
    Grodno = 'Grodno',
    Guestrow = 'Guestrow',
    Hamburg = 'Hamburg',
    Hannover = 'Hannover',
    Harz = 'Harz',
    Jena = 'Jena',
    JugendgemeinschaftSMH = 'JugendgemeinschaftSMH',
    JugendgemeinschaftUrgemeinde = 'JugendgemeinschaftUrgemeinde',
    Lausitz = 'Lausitz',
    Leipzig = 'Leipzig',
    Pasewalk = 'Pasewalk',
    Potsdam = 'Potsdam',
    SchwedtAngermuende = 'SchwedtAngermuende',
    Stuttgart = 'Stuttgart',
    UrgemeindeFriedensstadt = 'UrgemeindeFriedensstadt',
    Velten = 'Velten',
    Wiesbaden = 'Wiesbaden',
    WittenbergElster = 'WittenbergElster')

function = enum(Jugendleiter = 'Jugendleiter', Prediger = 'Prediger', Hauptjugendleiter = 'Hauptjugendleiter')
    

class Booking(models.Model):
    number = models.IntegerField()
    participant = models.ForeignKey(Participant)
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
    
    
    