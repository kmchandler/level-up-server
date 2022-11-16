from django.db import models
from models import Gamer, Event

class EventGamer(models.Model):

    gamer = models.ForeignKey(on_delete=models.CASCADE)
    event = models.ForeignKey(on_delete=models.CASCADE)
