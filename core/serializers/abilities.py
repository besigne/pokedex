from rest_framework import serializers
from core.models.ability import Abilities


class AbilitiesModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Abilities
        fields = "__all__"
