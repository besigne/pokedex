from django.db import models
from core.models.pokemons import Pokemons


class Evolutions(models.Model):
    name = models.CharField(max_length=50)
    pokemon = models.ManyToManyField(Pokemons)

    def __str__(self):
        return self.name
