from django.db import models
from django.utils.crypto import get_random_string



class User(models.Model):
    name = models.CharField("Name", max_length=50)
    ip_address = models.GenericIPAddressField()

    def __str__(self):
        return self.name


class Session(models.Model):
    session_id = models.CharField(
        "Session_ID", primary_key=True, max_length=50)
    participant = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    started_time = models.DateTimeField("Start Time", auto_now=True)
    end_time = models.DateField("End Time", blank=True, null=True)

    def __str__(self):
        return self.session_id

    def add_winner(self, user_id):
        pass

    def add_participant(self):
        pass


class Winner(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    session = models.ForeignKey(
        Session, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name


class Host(models.Model):
    name = models.CharField("Name", max_length=50)
    host_token = models.CharField(
        "Host Token", primary_key=True, max_length=50)
    session = models.ForeignKey(
        Session, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

    def create_session(self, input_session_id: str = None):
        if self.session is None:
            new_session_id = input_session_id
            if input_session_id is None:
                new_session_id = self._get_unused_session_token()
            tmp_session = Session.objects.create(session_id=new_session_id)
            self.session_id = tmp_session

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
