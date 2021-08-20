from rest_framework.viewsets import ModelViewSet
from core.model.ability import Abilitiy
from core.serializer.ability_serializer import AbilityModelSerializer


class AbilityModelViewSet(ModelViewSet):

    queryset = Abilitiy.objects.all()
    serializer_class = AbilityModelSerializer

