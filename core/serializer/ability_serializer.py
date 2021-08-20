from rest_framework import serializers
from core.model.ability import Abilitiy


class AbilityModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Abilitiy
        fields = "__all__"
