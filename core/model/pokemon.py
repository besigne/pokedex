from django.db import models
from core.model.ability import Ability
from core.model.evolution import Evolution
from core.model.type import Type


class Pokemon(models.Model):
    name = models.CharField(max_length=50)
    type = models.ManyToManyField(Type)
    abilities = models.ManyToManyField(Ability)
    evolution = models.ManyToManyField(Evolution, blank=True)

    def __str__(self):
        return self.name
