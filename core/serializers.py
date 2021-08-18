from rest_framework import serializers
from core.models import Pokemons, Abilities


class PokemonsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemons
        fields = "__all__"


class AbilitiesModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Abilities
        fields = "__all__"
