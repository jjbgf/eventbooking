'''
Created on 08.02.2015

@author: samuelstein
'''

from django.forms import ModelForm
from django import forms
from django.forms.models import inlineformset_factory
from zeltlager_registration.models import Participant, Address, Jugendgruppe
import datetime
from localflavor.de.forms import *

#class RegisterForm(ModelForm):
    
class ParticipantForm(ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(ParticipantForm, self).__init__(*args, **kwargs)
        # Overwrite model
        self.fields['jugendgruppe'] = forms.ModelChoiceField(queryset=Jugendgruppe.objects.all())
        self.fields['firstname'].label = "Vorname"
        self.fields['mail'] = forms.EmailField()
        self.fields['birth_date'] = forms.DateField(required=True, initial=datetime.date.today)
        self.fields['birth_place'] = forms.DateField(required=True, initial=datetime.date.today)
        #self.fields['bundesland'] = DEStateSelect()
        self.fields['postcode'] = DEZipCodeField()
               
    class Meta:
        model = Participant
        #exclude = ('zeltlager_durchgang',)
        #fields = ['firstname', 'name', 'jugendgruppe', 'mail', 'job', 'birth_date', 'birth_place', 'vegetarian', 'gender']
    
    
    
class AddressForm(ModelForm):
    
    class Meta:
        model = Address
        #exclude = ('Participant',)
        
        
RegisterFormSet = inlineformset_factory(Address, Participant, can_delete=True)