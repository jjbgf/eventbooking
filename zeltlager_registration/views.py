# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
import logging
from zeltlager_registration.forms import  ParticipantForm, RegisterFormSet
from zeltlager_registration.models import ZeltlagerDurchgang, Participant
from django.forms.models import inlineformset_factory
from django.views.decorators.http import require_http_methods

# Get an instance of a logger
logger = logging.getLogger(__name__)

@require_http_methods(["GET"])
def index(request):
    context = {'greeting': 'Hello, world. You\'re at the zeltlager registration index.'}
    return render(request, 'zeltlager_registration/index.html', context)

@require_http_methods(["POST"])
def save(request):
    
    # create a form instance and populate it with data from the request:
    form = ParticipantForm(request.POST)
    # check whether it's valid:
    logger.debug(form.is_valid())
        
    if form.is_valid():
        participant = form.save(commit=False)
        #participant_formset = RegisterFormSet(request.POST, instance=participant)
            
#             if participant_formset.is_valid():
#                 participant.save()
#                 participant_formset.save()
            
            #dirty hack
            #newitem = form.save(commit=False)
            #newitem.ZeltlagerDurchgang = ZeltlagerDurchgang.objects.get(id=1)
            #newitem.save()
            #form.cleaned_data['zeltlager_durchgang_id'] = 1
            #form.save()
            
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
        return HttpResponseRedirect('zeltlager_registration/thanks.html')

    return HttpResponse("saved")

@require_http_methods(["GET"])
def register (request):
    context = {'form' : ParticipantForm()}
    #context = {'formset' : RegisterFormSet()}
    return render(request, 'zeltlager_registration/register.html', context)
#     return render(request, 'zeltlager_registration/register.html')
    