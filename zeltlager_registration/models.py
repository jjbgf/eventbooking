# -*- coding: utf-8 -*-
from django.db import models
from django.utils.encoding import smart_unicode
from localflavor.de.de_states import STATE_CHOICES
from django.utils.translation import ugettext_lazy as _

GENDER_CHOICES = (('0', _('female')), ('1', _('male')))
SWIMMING_BADGE_CHOICES = (('Seepferdchen',_('seahorse')),('Bronze',_('bronze')),('Silber',_('silver')),('Gold',_('gold')),('Rettungsschwimmabzeichen',_('lifeguard')))
ROLE_CHOICES = (('Jugendleiter', _('youth leader')), ('Prediger', _('preacher')), ('Hauptjugendleiter', _('head youth leader')))
TRANSPORTATION_CHOICES = (('KFZ_Eigen', _('own car')),
    ('KFZ_mitfahrt', _('car passenger')),
    ('BusSMH', _('bus from SMH')),
    ('BusFS', _('bus from Friedensstadt')),
    ('Bahn', _('train')),
    ('Flugzeug', _('plane')),
    ('zuFuss', _('walking')),
    ('andere', _('other')),
    ('keine', _('none')))

class Address (models.Model):
    street = models.CharField(max_length=200, verbose_name=_('street'))
    street_additional = models.CharField(max_length=20, blank=True, verbose_name=_('street additional'))
    street_number = models.PositiveIntegerField(verbose_name=_('street number'))
    postcode = models.PositiveIntegerField(verbose_name=_('ZIP code'))
    city = models.CharField(max_length=200, verbose_name=_('city'))
    state = models.CharField(max_length=100, choices=STATE_CHOICES, verbose_name=_('state'))
    country = models.CharField(max_length=200, verbose_name=_('country'))
    
    class Meta:
        app_label = 'zeltlager_registration'
        verbose_name = verbose_name=_('address')
        verbose_name_plural = _('addresses')
        
    def __unicode__(self):
        return smart_unicode(self.street + ", " + str(self.street_number) + ", "+ str(self.postcode) +" "+ self.city)
    
class Jugendgruppe(models.Model):
    name = models.CharField(max_length=200)
    address = models.ForeignKey(Address, blank=True, default=None, verbose_name=_('address'))
    description = models.CharField(max_length=500, verbose_name=_('description'))
    # reference the jugendleiter (one to many)
    
    def __unicode__(self):
        return smart_unicode(self.name)
    
    class Meta:
        app_label = 'zeltlager_registration'
        verbose_name = _('youth group')
        verbose_name_plural = _('youth groups')

class ZeltlagerDurchgang(models.Model):
    number = models.IntegerField(primary_key=True, verbose_name=_('number'))
    name = models.CharField(max_length=100)
    address = models.ForeignKey(Address, blank=True, default=None, verbose_name=_('address'))
    start = models.DateTimeField(verbose_name=_('start'))
    end = models.DateTimeField(verbose_name=_('end'))
    capacity = models.IntegerField(verbose_name=_('capacity'))
    lagerleiter = models.CharField(max_length=200, verbose_name=_('head'))
    
    class Meta:
        app_label = 'zeltlager_registration'
        verbose_name = _('zeltlager pass')
        verbose_name_plural = _('zeltlager passes')

    def __unicode__(self):
        return smart_unicode(self.name)

class Participant(models.Model):
    name = models.CharField(max_length=200, verbose_name=_('sirname'))
    firstname = models.CharField(max_length=200, verbose_name=_('firstname'))
    zeltlager_durchgang = models.ForeignKey(ZeltlagerDurchgang, blank=False, default=None, verbose_name=_('zeltlager pass'))
    address = models.ForeignKey(Address, blank=False, default=None, verbose_name=_('address'))
    phone_number = models.CharField(max_length=200, blank=True, verbose_name=_('phone number'))
    mobile_number = models.CharField(max_length=200, blank=True, verbose_name=_('mobile number'))
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, verbose_name=_('gender'))
    position = models.CharField(max_length=20, choices=ROLE_CHOICES, blank=True, verbose_name=_('position'))
    jugendgruppe = models.CharField(max_length=200, blank=True, verbose_name=_('youth group'))
    mail = models.EmailField(max_length=254, blank=True, verbose_name=_('mail'))
    job = models.CharField(max_length=200, blank=True, verbose_name=_('job'))
    birth_date = models.DateField(verbose_name=_('birth date'))
    birth_place = models.CharField(max_length=200, verbose_name=_('birth place'))
    vegetarian = models.BooleanField(default=False, verbose_name=_('vegetarian'))
    restrictions = models.TextField(blank=True, verbose_name=_('restrictions'))
    skills = models.TextField(blank=True, verbose_name=_('skills'))
    legal_guardian = models.CharField(max_length=200, verbose_name=_('legal guardian'))
    legal_guardian_phone_number = models.CharField(max_length=200, verbose_name=_('phone number'))
    legal_guardian_mobile_number = models.CharField(max_length=200, verbose_name=_('mobile number'))
    insurance_company = models.CharField(max_length=200, verbose_name=_('insurance company'))
    insurance_number = models.PositiveIntegerField(verbose_name=_('insurance number'))
    main_insurant = models.CharField(max_length=200, verbose_name=_('main insurant'))
    main_insurant_birthdate = models.DateField(verbose_name=_('birth date'))
    main_insurant_address = models.CharField(max_length=200, verbose_name=_('address'))
    main_insurant_employer = models.CharField(max_length=200, verbose_name=_('employer'))
    tetanus_immunization = models.DateField(blank=True, null=True, verbose_name=_('tetanus immunization'))
    remember_me_about_medicine = models.TextField(blank=True, verbose_name=_('remmeber me about following medicine'))
    swimming_badge = models.CharField(max_length=50, blank=True, choices=SWIMMING_BADGE_CHOICES, verbose_name=_('swimming badge'))
    allow_separation_in_groups = models.BooleanField(default=False, verbose_name=_('allow seperation in groups'))
    additional_participants_same_household = models.CharField(max_length=200, blank=True, verbose_name=_('additional participants from same household'))
    partial_participant = models.BooleanField(default=False, verbose_name=_('partial participant'))
    partial_start = models.DateField(blank=True, null=True, verbose_name=_('partial start'))
    partial_end = models.DateField(blank=True, null=True, verbose_name=_('partial end'))
    alternative_zeltlager_durchgang = models.ForeignKey(ZeltlagerDurchgang, related_name='+', blank=True, default=None, null=True, verbose_name=_('alternative zeltlager pass'))
    preferred_work = models.TextField(blank=True, verbose_name=_('preferred work'))
    activities_i_liked = models.TextField(blank=True, verbose_name=_('activities I liked'))
    things_i_can_provide = models.TextField(blank=True, verbose_name=_('things I can provide'))
    
    arrival = models.DateTimeField(verbose_name=_('arrival'))
    departure = models.DateTimeField(verbose_name=_('departure'))
    transportationBegin = models.CharField(max_length=20, blank=False, verbose_name=_('depart from'))
    transportationBeginMethod = models.CharField(max_length=20, choices=TRANSPORTATION_CHOICES, default='keine', verbose_name=_('transportation outward method'))
    transportationEnd = models.CharField(max_length=20, blank=False, verbose_name=_('return to'))
    transportationEndMethod = models.CharField(max_length=20, choices=TRANSPORTATION_CHOICES, default='keine', verbose_name=_('transportation return method'))
    
    class Meta:
        app_label = 'zeltlager_registration'
        verbose_name = _('participant')
        verbose_name_plural = _('participants')

    def __unicode__(self):
        return smart_unicode(self.firstname + ", " + self.name)
