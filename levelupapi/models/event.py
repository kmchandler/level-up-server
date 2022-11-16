from django.db import models
from models import Game, Gamer
from datetime import date
from django.utils.timezone import now


class Event(models.Model):

    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    date = models.DateField(default=date.today)
    time = models.DateTimeField(default=now, editable=False)
    organizer = models.ForeignKey(Gamer, on_delete=models.CASCADE)
