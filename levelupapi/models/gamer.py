from django.db import models


class Gamer(models.Model):

    bio = models.CharField(max_length=100)
    uid = models.CharField(max_length=50)
