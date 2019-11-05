from django.db import models

# Create your models here.
class RaffleSession(models.Model):

    def __str__(self):
        return f"Key: {self.session_key} Name: {self.session_name}" 

    session_key = models.CharField(max_length=10, primary_key=True)
    session_name = models.CharField(max_length=200)

class Participant(models.Model):

    def __str__(self):
        return f"Session: {self.session} Name: {self.participant_name} Key: {participant_id}" 

    session = models.ForeignKey(RaffleSession, on_delete=models.CASCADE)
    participant_name = models.CharField(max_length=200)
    participant_id = models.AutoField(primary_key=True)
    hasWon = models.BooleanField(default=False)
