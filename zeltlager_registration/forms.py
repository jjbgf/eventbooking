'''
Created on 08.02.2015

@author: samuelstein
'''

from django.forms import ModelForm
from django import forms
from django.forms.models import inlineformset_factory
from zeltlager_registration.models import Participant, Address, Jugendgruppe
import datetime
from localflavor.de.forms import DEZipCodeField
from django.core.exceptions import ValidationError
from datetimewidget.widgets import DateWidget


#class RegisterForm(ModelForm):
    
class ParticipantForm(ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(ParticipantForm, self).__init__(*args, **kwargs)
        # Overwrite model
        self.fields['jugendgruppe'] = forms.ModelChoiceField(queryset=Jugendgruppe.objects.all())
        self.fields['firstname'].label = "Vorname"
        self.fields['mail'] = forms.EmailField()
        #self.fields['birth_date'] = forms.DateField(required=True, initial=datetime.date.today())
        self.fields['postcode'] = DEZipCodeField()
        
        
    def clean(self):
        cleaned_data = super(ParticipantForm, self).clean()
        mail = cleaned_data.get("mail")
        
        if not mail:
            raise ValidationError("Keine E-Mail-Adresse angegeben")
               
    class Meta:
        model = Participant
        widgets = {
            #Use localization and bootstrap 3
            'birth_date': DateWidget(attrs={'id':"birth_date"}, usel10n = True, bootstrap_version=3),
            'main_insurant_birthdate': DateWidget(attrs={'id':"main_insurant_birthdate"}, usel10n = True, bootstrap_version=3),
            'tetanus_immunization': DateWidget(attrs={'id':"tetanus_immunization"}, usel10n = True, bootstrap_version=3),
            'partial_start': DateWidget(attrs={'id':"partial_start"}, usel10n = True, bootstrap_version=3),
            'partial_end': DateWidget(attrs={'id':"partial_end"}, usel10n = True, bootstrap_version=3)
            }
#         exclude = ()
#         fields = []
    
    
class AddressForm(ModelForm):
    
    class Meta:
        model = Address
        #exclude = ('Participant',)
        
        
RegisterFormSet = inlineformset_factory(Address, Participant)