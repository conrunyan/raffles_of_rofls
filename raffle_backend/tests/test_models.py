from django.test import TestCase
from raffle_backend.models import (
    User,
    Winner,
    Session,
    Host
)


class TestUser(TestCase):
    def test_base_constructor(self):
        user = User(name='Fred', ip_address='127.0.0.1')
        self.assertTrue(isinstance(user, User))
        self.assertEqual('Fred', str(user))


class TestHost(TestCase):

    def test_constructor_without_session_id(self):
        host = Host(name='Velma', host_token='AkSefj90j#89wj4$GH9s4S)$Fj')
        self.assertTrue(isinstance(host, Host))
        self.assertEqual('Velma', str(host))

    def test_create_session_does_not_exist_yet(self):
        host = Host(name='Velma', host_token='AkSefj90j#89wj4$GH9s4S)$Fj')
        expected_id = 'ABC123'

        self.assertIsNone(host.session_id)
        host.create_session(expected_id)
        self.assertEqual(expected_id, host.session.session_id)

    def test_create_session_already_exists(self):
        host = Host(name='Velma', host_token='AkSefj90j#89wj4$GH9s4S)$Fj')
        fake_id = 'ABC123'

        self.assertIsNone(host.session_id)
        host.create_session()
        # Create another one
        host.create_session(fake_id)
        self.assertNotEqual(fake_id, host.session.session_id)


class TestSession(TestCase):
    pass


class TestWinner(TestCase):
    pass
