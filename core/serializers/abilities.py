from rest_framework import serializers
from core.models.abilities import Abilities


class AbilitiesModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Abilities
        fields = "__all__"
