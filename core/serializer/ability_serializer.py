from rest_framework import serializers
from core.model.ability import Ability


class AbilityModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ability
        fields = "__all__"
