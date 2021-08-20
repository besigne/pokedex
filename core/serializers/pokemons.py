from rest_framework import serializers
from core.models.pokemon import Pokemons


class PokemonsModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pokemons
        fields = "__all__"

