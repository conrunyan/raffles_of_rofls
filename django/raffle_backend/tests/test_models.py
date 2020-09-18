from django.db import transaction
from django.db.utils import IntegrityError
from django.test import TestCase
from raffle_backend.models import (
    Participant,
    Winner,
    Session,
    Host
)


class TestUser(TestCase):
    def test_base_constructor(self):
        host = Host.objects.create(name='Fred', host_token='apowief2q[-90j')
        session = Session.objects.create(session_id='ABC123', host_id=host)
        user = Participant(
            name='Fred', ip_address='127.0.0.1', session=session)
        self.assertTrue(isinstance(user, Participant))
        self.assertEqual('Fred', str(user))


class TestHost(TestCase):

    def test_constructor_without_session_id(self):
        host = Host.objects.create(name='Velma', host_token='AP(IJW$W)G(J')
        self.assertTrue(isinstance(host, Host))
        self.assertEqual('Velma', str(host))

    def test_create_session_does_not_exist_yet(self):
        host = Host.objects.create(name='Velma', host_token='AP(IJW$W)G(Jj')
        expected_id = 'ABC123'

        with self.assertRaises(Session.DoesNotExist):
            self.assertIsNone(Session.objects.get(session_id=expected_id))
        session = host.create_session(expected_id)
        self.assertEqual(expected_id, session.session_id)

    def test_create_session_already_exists(self):
        host = Host.objects.create(name='Velma', host_token='AP(IJW$W)G(Jj')
        initial_id = 'ABC123'

        with self.assertRaises(Session.DoesNotExist):
            self.assertIsNone(Session.objects.get(session_id=initial_id))
        host.create_session(initial_id)
        # Create another one
        host.create_session(initial_id)
        self.assertEqual(1, len(Session.objects.filter(session_id=initial_id)))


class TestSession(TestCase):

    def test_constructor(self):
        host = Host.objects.create(name='Fred', host_token='AP(IJW$W)G(J')
        session = Session(session_id='ABC123', host_id=host)
        self.assertTrue(isinstance(session, Session))
        self.assertEqual('ABC123', str(session))

    def test_add_winner_first_winner(self):
        host = Host.objects.create(name='Fred', host_token='AP(IJW$W)G(J')
        session = Session.objects.create(session_id='ABC123', host_id=host)
        user = Participant.objects.create(
            name='Shaggy', ip_address='0.0.0.0', session=session)

        with self.assertRaises(Winner.DoesNotExist):
            self.assertIsNone(Winner.objects.get(user=user))

        session.add_winner(user_instance=user)

        self.assertIsNotNone(Winner.objects.get(user=user))

    def test_add_winner_second_winner(self):
        host = Host.objects.create(name='Fred', host_token='AP(IJW$W)G(J')
        session = Session.objects.create(session_id='ABC123', host_id=host)
        user = Participant.objects.create(
            name='Shaggy', ip_address='0.0.0.0', session=session)
        user2 = Participant.objects.create(
            name='Daphne', ip_address='0.0.0.1', session=session)

        session.add_winner(user_instance=user)
        session.add_winner(user_instance=user2)

        self.assertIsNotNone(Winner.objects.get(user=user))
        self.assertIsNotNone(Winner.objects.get(user=user2))
        self.assertEqual(2, len(Winner.objects.all()))

    def test_add_winner_duplicate_winner(self):
        host = Host.objects.create(name='Fred', host_token='AP(IJW$W)G(J')
        session = Session.objects.create(session_id='ABC123', host_id=host)
        user = Participant.objects.create(
            name='Shaggy', ip_address='0.0.0.0', session=session)
        # breakpoint()
        session.add_winner(user_instance=user)
        # https://stackoverflow.com/questions/21458387/transactionmanagementerror-you-cant-execute-queries-until-the-end-of-the-atom
        with transaction.atomic():
            session.add_winner(user_instance=user)

        self.assertIsNotNone(Winner.objects.get(user=user))
        self.assertEqual(1, len(Winner.objects.all()))

    def test_add_participant_first_participant(self):
        host = Host.objects.create(name='Fred', host_token='AP(IJW$W)G(J')
        session = Session.objects.create(session_id='ABC123', host_id=host)
        session.add_participant(
            username='Velma', ip_addr='0.0.0.0')
        self.assertIsNotNone(Participant.objects.get(
            name='Velma', ip_address='0.0.0.0', session=session))

    def test_add_participant_not_first_participant(self):
        host = Host.objects.create(name='Fred', host_token='AP(IJW$W)G(J')
        session = Session.objects.create(session_id='ABC123', host_id=host)
        session.add_participant(
            username='Velma', ip_addr='0.0.0.0')
        session.add_participant(
            username='Fred', ip_addr='0.0.0.1')
        self.assertEqual(2, len(Participant.objects.filter(session=session)))

    def test_add_participant_duplicate_participant(self):
        host = Host.objects.create(name='Fred', host_token='AP(IJW$W)G(J')
        session = Session.objects.create(session_id='ABC123', host_id=host)
        session.add_participant(
            username='Velma', ip_addr='0.0.0.0')
        with transaction.atomic():
            session.add_participant(
                username='Scrappy', ip_addr='0.0.0.0')
        self.assertEqual(1, len(Participant.objects.filter(session=session)))


class TestWinner(TestCase):
    def test_constructor(self):
        host = Host.objects.create(name='Fred', host_token='AP(IJW$W)G(J')
        session = Session.objects.create(session_id='ABC123', host_id=host)
        tmp_user = Participant.objects.create(
            name='Scooby', ip_address='0.0.0.0', session=session)
        winner = Winner.objects.create(user=tmp_user, session=session)
