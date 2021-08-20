from rest_framework import serializers
from core.model.pokemon import Pokemon


class PokemonModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pokemon
        fields = "__all__"

