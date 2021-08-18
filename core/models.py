from django.db import models


class Pokemons(models.Model):
    name = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name


class Evolution(models.Model):
    name = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name


class Abilities(models.Model):
    name = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Pokemon_has_abilities(models.Model):
    pokemon = models.ForeignKey(Pokemons, on_delete=models.PROTECT)
    ability = models.ForeignKey(Abilities, on_delete=models.PROTECT)

    def __str__(self):
        return self.id


class Pokemon_evolve_to(models.Model):
    pokemon = models.ForeignKey(Pokemons, on_delete=models.PROTECT)
    evolution = models.ForeignKey(Evolution, on_delete=models.PROTECT)
