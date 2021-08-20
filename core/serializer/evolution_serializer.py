from rest_framework import serializers
from core.model.evolution import Evolution


class EvolutionModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Evolution
        fields = "__all__"
