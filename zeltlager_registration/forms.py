'''
Created on 08.02.2015

@author: samuelstein
'''

from django.forms import ModelForm
from django import forms
from zeltlager_registration.models import Participant, Address, Jugendgruppe
import datetime
from localflavor.de.forms import DEZipCodeField
from django.core.exceptions import ValidationError
from datetimewidget.widgets import DateWidget, DateTimeWidget


#class RegisterForm(ModelForm):
    
class ParticipantForm(ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(ParticipantForm, self).__init__(*args, **kwargs)
        # Overwrite model
        self.fields['jugendgruppe'] = forms.ModelChoiceField(queryset=Jugendgruppe.objects.all())
        self.fields['mail'] = forms.EmailField()
        #self.fields['birth_date'] = forms.DateField(required=True, initial=datetime.date.today())
        
        
    #def clean(self):
     #   cleaned_data = super(RegisterForm, self).clean()
      #  mail = cleaned_data.get("mail")
        
       # if not mail:
        #    raise ValidationError("Keine E-Mail-Adresse angegeben")
               
    class Meta:
        model = Participant
        exclude = ['address']
        widgets = {
            #Use localization and bootstrap 3
            'birth_date': DateWidget(attrs={'id':"birth_date"}, usel10n = True, bootstrap_version=3),
            'main_insurant_birthdate': DateWidget(attrs={'id':"main_insurant_birthdate"}, usel10n = True, bootstrap_version=3),
            'tetanus_immunization': DateWidget(attrs={'id':"tetanus_immunization"}, usel10n = True, bootstrap_version=3),
            'partial_start': DateWidget(attrs={'id':"partial_start"}, usel10n = True, bootstrap_version=3),
            'partial_end': DateWidget(attrs={'id':"partial_end"}, usel10n = True, bootstrap_version=3),
            'arrival': DateTimeWidget(attrs={'id':"arrival"}, usel10n = True, bootstrap_version=3),
            'departure': DateTimeWidget(attrs={'id':"departure"}, usel10n = True, bootstrap_version=3)
            }
    
class AddressForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddressForm, self).__init__(*args, **kwargs)
        # Overwrite model
        self.fields['postcode'] = DEZipCodeField()
        
    class Meta:
        model = Address
        
#RegisterFormSet = inlineformset_factory(Address, Participant)