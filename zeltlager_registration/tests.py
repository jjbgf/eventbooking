# -*- coding: utf-8 -*-
from django.test import TestCase
import logging
from django.test import Client
from django.contrib.auth.models import User
from django.core.management import execute_from_command_line
from zeltlager_registration.models import Jugendgruppe, ZeltlagerDurchgang


logger = logging.getLogger(__name__)

class HTTPResourceTestCase(TestCase):
    
    def setUp(self):
        TestCase.setUp(self)
        self.csrf_client = Client(enforce_csrf_checks=False)
        execute_from_command_line(["manage.py", "loaddata", "initial_data.yaml"])

    
    def testHTTPPostMethod(self):
        # Check if only GET is allowed
        response = self.csrf_client.post('/zeltlager/register/')
        self.assertEqual(response.status_code, 405, 'HTTP POST is allowed')
    
    def testInitialUserCreated(self):
        u = User.objects.get(username='admin')
        self.assertEqual(u.id, 1, 'created initial user')
        
    def testInitialJugendgruppeCreated(self):
        j = Jugendgruppe.objects.get(name='Dresden')
        self.assertEqual(j.name, 'Dresden', 'created jugendgruppe')
        
    def testInitialZeltlagerCreated(self):
        z = ZeltlagerDurchgang.objects.get(name='3. Zeltlager Friedensstadt')
        self.assertEqual(z.name, '3. Zeltlager Friedensstadt', 'created zeltlager')