from django.test import TestCase

from rest_framework.test import APITestCase
from rest_framework import status
from raffle_backend.models import (
    Session,
    Host,
    Participant
)

class TestParticipant(APITestCase):
    def setUp(self):
        self.host = Host.objects.create(name='Fred', host_token='AP(IJW$W)G(J')
        self.session = Session.objects.create(session_id='ABC123', host_id=self.host)
    
    def test_post_request_add_participant_existing_session(self):
        self.fail()
    
    def test_post_request_add_participant_no_session(self):
        self.fail()
    
    def test_post_request_add_participant_bad_request(self):
        data = {'name': 'DabApps'}
        response = self.client.post('/sessions/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        with self.assertRaises(Participant.DoesNotExist):
            Participant.objects.get(session=self.session)

class TestHost(APITestCase):
    pass

class TestSession(APITestCase):
    pass
