'''
Created on 08.02.2015

@author: samuelstein
'''

from django.forms import ModelForm
from django import forms
from django.forms.models import inlineformset_factory
from zeltlager_registration.models import Participant, Address
import datetime

#class RegisterForm(ModelForm):
    
class ParticipantForm(ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(ParticipantForm, self).__init__(*args, **kwargs)
        # Overwrite model
        self.fields['jugendgruppe'] = forms.CharField(max_length=50, widget=forms.Select(choices=[('Berlin SMH', 'Friedensstadt')]))
        self.fields['firstname'].label = "Vorname"
        self.fields['mail'] = forms.EmailField()
        self.fields['birth_date'] = forms.DateField(required=True, initial=datetime.date.today)
        self.fields['birth_place'] = forms.DateField(required=True, initial=datetime.date.today)
        #dirty hack
        #self.fields['insurance_number'].required=False
               
    class Meta:
        model = Participant
        exclude = ('zeltlager_durchgang',)
        fields = ['firstname', 'name', 'jugendgruppe', 'mail', 'job', 'birth_date', 'birth_place', 'vegetarian']
    
    
    
class AddressForm(ModelForm):
    
    class Meta:
        model = Address
        #exclude = ('Participant',)
        
        
RegisterFormSet = inlineformset_factory(Address, Participant, can_delete=True)