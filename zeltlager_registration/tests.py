from django.test import TestCase
import logging
from django.test import Client

logger = logging.getLogger(__name__)

class HTTPResourceTestCase(TestCase):
    
    def setUp(self):
        TestCase.setUp(self)
        self.csrf_client = Client(enforce_csrf_checks=False)
    
    def testHTTPPostMethod(self):
        # Check if only GET is allowed
        response = self.csrf_client.post('/zeltlager/register/')
        logger.debug(response)
        self.assertEqual(response.status_code, 405, 'HTTP POST is allowed')
    