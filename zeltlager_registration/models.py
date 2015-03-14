# -*- coding: utf-8 -*-
from django.db import models
from django.utils.encoding import smart_unicode
from localflavor.de.de_states import STATE_CHOICES

GENDER_CHOICES = (('0', 'weiblich'), ('1', 'männlich'))
SWIMMING_BADGE_CHOICES = (('Seepferdchen','Seepferdchen'),('Bronze','Deutsches Jugendschwimmabzeichen – Bronze'),('Silber','Deutsches Jugendschwimmabzeichen – Silber'),('Gold','Deutsches Jugendschwimmabzeichen – Gold'),('Rettungsschwimmabzeichen','Rettungsschwimmabzeichen'))
ROLE_CHOICES = (('Jugendleiter', 'Jugendleiter'), ('Prediger', 'Prediger'), ('Hauptjugendleiter', 'Hauptjugendleiter'))

class Address (models.Model):
    street = models.CharField(max_length=200)
    street_additional = models.CharField(max_length=20, blank=True)
    street_number = models.PositiveIntegerField()
    postcode = models.PositiveIntegerField()
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=100, choices=STATE_CHOICES)
    country = models.CharField(max_length=200)
    
    class Meta:
        app_label = 'zeltlager_registration'
        verbose_name = 'Adresse'
        verbose_name_plural = 'Adressen'
        
    def __unicode__(self):
        return smart_unicode(self.street + ", " + str(self.street_number) + ", "+ str(self.postcode) +" "+ self.city)
    
class Jugendgruppe(models.Model):
    name = models.CharField(max_length=200)
    address = models.ForeignKey(Address, blank=True, default=None)
    description = models.CharField(max_length=500)
    # reference the jugendleiter (one to many)
    
    def __unicode__(self):
        return smart_unicode(self.name)
    
    class Meta:
        app_label = 'zeltlager_registration'
        verbose_name = 'Jugendgruppe'
        verbose_name_plural = 'Jugendgruppen'

class ZeltlagerDurchgang(models.Model):
    number = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.ForeignKey(Address, blank=True, default=None)
    start = models.DateTimeField()
    end = models.DateTimeField()
    capacity = models.IntegerField()
    lagerleiter = models.CharField(max_length=200)
    
    class Meta:
        app_label = 'zeltlager_registration'
        verbose_name = 'Zeltlagerdurchgang'
        verbose_name_plural = 'Zeltlagerdurchgänge'

    def __unicode__(self):
        return smart_unicode(self.name)

class Participant(models.Model):
    name = models.CharField(max_length=200)
    firstname = models.CharField(max_length=200)
    zeltlager_durchgang = models.ForeignKey(ZeltlagerDurchgang, blank=False, default=None)
    address = models.ForeignKey(Address, blank=False, default=None)
    phone_number = models.CharField(max_length=200, blank=True)
    mobile_number = models.CharField(max_length=200, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    position = models.CharField(max_length=20, choices=ROLE_CHOICES, blank=True)
    jugendgruppe = models.CharField(max_length=200, blank=True)
    mail = models.EmailField(max_length=254, blank=True)
    job = models.CharField(max_length=200, blank=True)
    birth_date = models.DateField()
    birth_place = models.CharField(max_length=200)
    vegetarian = models.BooleanField(default=False)
    restrictions = models.TextField(blank=True)
    skills = models.TextField(blank=True)
    legal_guardian = models.CharField(max_length=200)
    legal_guardian_phone_number = models.CharField(max_length=200)
    legal_guardian_mobile_number = models.CharField(max_length=200)
    insurance_company = models.CharField(max_length=200)
    insurance_number = models.PositiveIntegerField()
    main_insurant = models.CharField(max_length=200)
    main_insurant_birthdate = models.DateField()
    main_insurant_address = models.CharField(max_length=200)
    main_insurant_employer = models.CharField(max_length=200)
    tetanus_immunization = models.DateField(blank=True, null=True)
    remember_me_about_medicine = models.TextField(blank=True)
    swimming_badge = models.CharField(max_length=50, blank=True, choices=SWIMMING_BADGE_CHOICES)
    allow_separation_in_groups = models.BooleanField(default=False)
    additional_participants_same_household = models.CharField(max_length=200, blank=True)
    partial_participant = models.BooleanField(default=False)
    partial_start = models.DateField(blank=True, null=True)
    partial_end = models.DateField(blank=True, null=True)
    alternative_zeltlager_durchgang = models.ForeignKey(ZeltlagerDurchgang, related_name='+', blank=True, default=None, null=True)
    preferred_work = models.TextField(blank=True)
    activities_i_liked = models.TextField(blank=True)
    things_i_can_provide = models.TextField(blank=True)
    arrival_by = models.CharField(max_length=200)
    
    class Meta:
        app_label = 'zeltlager_registration'
        verbose_name = 'Teilnehmer'
        verbose_name_plural = 'Teilnehmer'

    def __unicode__(self):
        return smart_unicode(self.firstname + ", " + self.name)
