# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import  HttpResponseRedirect
from django.contrib import messages
from honeypot.decorators import check_honeypot
from zeltlager_registration.models import Address, Participant
import logging
from zeltlager_registration.forms import  ParticipantForm, AddressForm
from django.views.decorators.http import require_http_methods

# Get an instance of a logger
logger = logging.getLogger(__name__)

@require_http_methods(["GET"])
def index(request):
    context = {'greeting': 'Hello, world. You\'re at the zeltlager registration index.'}
    return render(request, 'zeltlager_registration/index.html', context)

@require_http_methods(["POST"])
@check_honeypot(field_name='age')
def save(request):
    
    #dirty hack
    #see: https://djangosnippets.org/snippets/1248/
    address = Address()
    address.id = None
    
    participant = Participant()
    participant.id = None
    
    # create a form instance and populate it with data from the request:
    addressForm = AddressForm(request.POST, instance=address)
    participantForm = ParticipantForm(request.POST, instance=participant)
    
    # check whether it's valid:
    logger.debug('forms valid: '+ str(addressForm.is_valid() + participantForm.is_valid()))
        
    if addressForm.is_valid() and participantForm.is_valid():
        
        # commit = false doesn't save to DB.
        address = addressForm.save(commit=False)
        address.save()
        participant = participantForm.save(commit=False)
        participant.address = address
        participant.save()
            
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        messages.success(request, 'Vielen Dank.\nDeine Daten wurden erfolgreich gespeichert.')
        return HttpResponseRedirect('/zeltlager/thanks/')

    # Redisplay the form.
    messages.error(request, 'Bitte fülle alle Felder aus!')
    return HttpResponseRedirect('/zeltlager/register/')

@require_http_methods(["GET"])
def register (request):
    context = {'addressForm' : AddressForm(), 'participantForm' : ParticipantForm()}
    return render(request, 'zeltlager_registration/register.html', context)
    