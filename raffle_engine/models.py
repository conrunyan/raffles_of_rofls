from django.db import models

# Create your models here.
class RaffleSession(models.Model):
    session_key = models.CharField(max_length=10, primary_key=True)
    session_name = models.CharField(max_length=200)

class Participant(models.Model):
    session = models.ForeignKey(RaffleSession, on_delete=models.CASCADE)
    participant_name = models.CharField(max_length=200)
    participant_id = models.AutoField(primary_key=True)
    hasWon = models.BooleanField(default=False)
