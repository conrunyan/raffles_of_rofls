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
    def create_winner(self, name: str, ip_addr:  str = '0.0.0.0'):
        tmp_user = User.objects.create(name=name, ip_address=ip_addr)
        return Winner.objects.create(user=tmp_user)

    def test_constructor(self):
        session = Session('ABC123')
        self.assertTrue(isinstance(session, Session))
        self.assertEqual('ABC123', str(session))

    def test_add_winner_first_winner(self):
        session = Session('ABC123')
        winner = self.create_winner('Shaggy')
        self.assertIsNone(session.winner)
        session.add_winner(winner)
        self.assertEqual(winner, session.winner)
        


class TestWinner(TestCase):
    def test_constructor(self):
        session = Session.objects.create(session_id='ABC123')
        tmp_user = User.objects.create(name='Scooby', ip_address='0.0.0.0')
        winner = Winner.objects.create(user=tmp_user, session=session)
