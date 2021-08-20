from rest_framework import serializers
from core.models.evolution import Evolutions


class EvolutionModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Evolutions
        fields = "__all__"
