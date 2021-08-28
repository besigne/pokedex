from rest_framework.viewsets import ModelViewSet
from core.model.ability import Ability
from core.serializer.ability_serializer import AbilityModelSerializer


class AbilityModelViewSet(ModelViewSet):

    queryset = Ability.objects.all()
    serializer_class = AbilityModelSerializer

