from django.db import models


class User(models.Model):
    name = models.CharField("Name", max_length=50)
    ip_address = models.GenericIPAddressField()

    def __str__(self):
        return self.name


class Winner(models.Model):
    name = models.CharField("Name", max_length=50)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Session(models.Model):
    session_id = models.CharField(
        "Session_ID", primary_key=True, max_length=50)
    participant = models.ForeignKey(User, on_delete=models.CASCADE)
    started_time = models.DateTimeField("Start Time", auto_now=True)
    end_time = models.DateField("End Time")
    winner = models.ForeignKey(Winner, on_delete=models.CASCADE)

    def __str__(self):
        return self.session_id

    def get_winners(self):
        pass

    def add_winner(self, user_id):
        pass

    def get_participants(self):
        pass

    def add_participants(self):
        pass

class Host(models.Model):
    name = models.CharField("Name", max_length=50)
    host_token = models.CharField("Host Token", primary_key=True, max_length=50)
    session_id = models.ForeignKey(Session, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_session(self):
        pass
