# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from zeltlager_registration.models import Address, Participant
import logging
from zeltlager_registration.forms import  ParticipantForm, AddressForm
from django.views.decorators.http import require_http_methods

# Get an instance of a logger
logger = logging.getLogger('zeltlager_registration')

@require_http_methods(["GET"])
def index(request):
    context = {'greeting': 'Hello, world. You\'re at the zeltlager registration index.'}
    return render(request, 'zeltlager_registration/index.html', context)

@require_http_methods(["POST"])
def save(request):
    
    #dirty dirty hack
    addresss = Address()
    addresss.id = None
    
    participantt = Participant()
    participantt.id = None
    
    # create a form instance and populate it with data from the request:
    addressForm = AddressForm(request.POST, instance=addresss)
    participantForm = ParticipantForm(request.POST, instance=participantt)
    
    # check whether it's valid:
    logger.debug('is form valid: '+ str(addressForm.is_valid()))
        
    #addressForm.clean()
        
    if addressForm.is_valid():
            
        address = addressForm.save(commit=False)
        address.save()
        participant = participantForm.save(commit=False)
        participant.address = address
        participant.save()
            
            # process the data in form.cleaned_data as required
        return render(request, 'zeltlager_registration/thanks.html')

    return HttpResponse("validation errors found")

@require_http_methods(["GET"])
def register (request):
    context = {'addressForm' : AddressForm(), 'participantForm' : ParticipantForm()}
    return render(request, 'zeltlager_registration/register.html', context)
    