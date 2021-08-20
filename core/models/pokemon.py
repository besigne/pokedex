from django.db import models
from core.models.ability import Abilities
from core.models.evolution import Evolutions


class Pokemons(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=30)
    abilities = models.ManyToManyField(Abilities)
    evolution = models.ManyToManyField(Evolutions)

    def __str__(self):
        return self.name
