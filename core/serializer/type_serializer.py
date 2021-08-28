from rest_framework import serializers
from core.model.type import Type


class TypeModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Type
        fields = "__all__"
