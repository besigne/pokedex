from django.db import models
from core.model.ability import Abilitiy
from core.model.evolution import Evolution


class Pokemon(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=30)
    abilities = models.ManyToManyField(Abilitiy)
    evolution = models.ManyToManyField(Evolution)

    def __str__(self):
        return self.name
