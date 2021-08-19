from django.db import models


class Pokemons(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=30)

    def __str__(self):
        return self.name
