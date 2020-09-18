import logging

from django.db import models
from django.utils.crypto import get_random_string
from django.db.utils import IntegrityError

logger = logging.getLogger(__name__)


class Participant(models.Model):
    name = models.CharField("Name", max_length=50)
    ip_address = models.GenericIPAddressField()
    logger.debug(
        f'New User object created: Name - {name}, IP Address - {ip_address}')
    session = models.ForeignKey('Session', on_delete=models.CASCADE)

    class Meta:
        unique_together = (('ip_address', 'session'))

    def __str__(self):
        return self.name


class Winner(models.Model):
    user = models.ForeignKey(Participant, on_delete=models.CASCADE)
    session = models.ForeignKey(
        'Session', on_delete=models.CASCADE, blank=True, null=True)

    # https://stackoverflow.com/questions/16800375/how-can-set-two-primary-key-fields-for-my-models-in-django
    class Meta:
        unique_together = (('user', 'session'),)

    def __str__(self):
        return f'Winner - Name: {self.user} Session: {self.session}'


class Session(models.Model):
    session_id = models.CharField(
        "Session_ID", primary_key=True, max_length=50)
    started_time = models.DateTimeField("Start Time", auto_now=True)
    end_time = models.DateField("End Time", blank=True, null=True)
    host_id = models.ForeignKey(
        'Host', on_delete=models.CASCADE)

    def __str__(self):
        return self.session_id

    def add_winner(self, user_instance):
        try:
            logger.info(
                f'Adding new Winner to Session: User - {user_instance}, Session - {self}')
            return Winner.objects.create(user=user_instance, session=self)
        except IntegrityError:
            logger.warning(f'Tried to add duplicate Winner to current session')

    def add_participant(self, username: str, ip_addr: str):
        # DONE: participant cannot be added if another user with the same IP address is already in the session
        try:
            logger.info(
                f'Adding User {username} at IP {ip_addr} to current session {self}')
            return Participant.objects.create(name=username, ip_address=ip_addr, session=self)
        except IntegrityError:
            # TODO: Have this raise an exception so I can catch it in the view
            logger.warning(
                f'Tried to add duplicate user {username}:{ip_addr} to current session.')


class Host(models.Model):
    name = models.CharField("Name", max_length=50)
    host_token = models.CharField(
        "Host Token", primary_key=True, max_length=50)

    def __str__(self):
        return self.name

    def create_session(self, input_session_id: str = None):
        try:
            Session.objects.get(host_id=self)
            logger.warning(f'Session for {self} already exists')
        except Session.DoesNotExist:
            new_session_id = input_session_id
            if input_session_id is None:
                new_session_id = self._get_unused_session_token()
            tmp_session = Session.objects.create(session_id=new_session_id, host_id=self)
            return tmp_session

    def _get_unused_session_token(self):
        NUM_CHARS = 6
        token = None
        token_already_exists = True
        # Loop until we find a new token
        while token_already_exists:
            token = get_random_string(length=NUM_CHARS).upper()
            try:
                Session.objects.get(session_id=token)
            except Session.DoesNotExist:
                token_already_exists = False

        return token
