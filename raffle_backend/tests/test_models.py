from django.db import transaction
from django.db.utils import IntegrityError
from django.test import TestCase
from raffle_backend.models import (
    User,
    Winner,
    Session,
    Host
)


class TestUser(TestCase):
    def test_base_constructor(self):
        session = Session.objects.create(session_id='ABC123')
        user = User(name='Fred', ip_address='127.0.0.1', session=session)
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

    def test_constructor(self):
        session = Session('ABC123')
        self.assertTrue(isinstance(session, Session))
        self.assertEqual('ABC123', str(session))

    def test_add_winner_first_winner(self):
        session = Session.objects.create(session_id='ABC123')
        user = User.objects.create(
            name='Shaggy', ip_address='0.0.0.0', session=session)

        with self.assertRaises(Winner.DoesNotExist):
            self.assertIsNone(Winner.objects.get(user=user))

        session.add_winner(user_instance=user)

        self.assertIsNotNone(Winner.objects.get(user=user))

    def test_add_winner_second_winner(self):
        session = Session.objects.create(session_id='ABC123')
        user = User.objects.create(
            name='Shaggy', ip_address='0.0.0.0', session=session)
        user2 = User.objects.create(
            name='Daphne', ip_address='0.0.0.1', session=session)

        session.add_winner(user_instance=user)
        session.add_winner(user_instance=user2)

        self.assertIsNotNone(Winner.objects.get(user=user))
        self.assertIsNotNone(Winner.objects.get(user=user2))
        self.assertEqual(2, len(Winner.objects.all()))

    def test_add_winner_duplicate_winner(self):
        session = Session.objects.create(session_id='ABC123')
        user = User.objects.create(
            name='Shaggy', ip_address='0.0.0.0', session=session)
        # breakpoint()
        session.add_winner(user_instance=user)
        try:
            with transaction.atomic():
                session.add_winner(user_instance=user)
            # self.fail('Duplicate winner addition did not throw IntegrityError')
        except IntegrityError:
            pass

        self.assertIsNotNone(Winner.objects.get(user=user))
        self.assertEqual(1, len(Winner.objects.all()))

    def test_add_participant_first_participant(self):
        session = Session.objects.create(session_id='ABC123')
        session.add_participant(
            username='Velma', ip_addr='0.0.0.0')
        self.assertIsNotNone(User.objects.get(
            name='Velma', ip_address='0.0.0.0', session=session))

    def test_add_participant_not_first_participant(self):
        session = Session.objects.create(session_id='ABC123')
        session.add_participant(
            username='Velma', ip_addr='0.0.0.0')
        session.add_participant(
            username='Fred', ip_addr='0.0.0.1')
        self.assertEqual(2, len(User.objects.filter(session=session)))

    def test_add_participant_duplicate_participant(self):
        session = Session.objects.create(session_id='ABC123')
        session.add_participant(
            username='Velma', ip_addr='0.0.0.0')
        with transaction.atomic():
            session.add_participant(
                username='Scrappy', ip_addr='0.0.0.0')
        self.assertEqual(1, len(User.objects.filter(session=session)))


class TestWinner(TestCase):
    def test_constructor(self):
        session = Session.objects.create(session_id='ABC123')
        tmp_user = User.objects.create(
            name='Scooby', ip_address='0.0.0.0', session=session)
        winner = Winner.objects.create(user=tmp_user, session=session)
