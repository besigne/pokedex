from rest_framework.viewsets import ModelViewSet
from core.models.abilities import Abilities
from core.serializers.abilities import AbilitiesModelSerializer


class AbilitiesModelViewSet(ModelViewSet):
    queryset = Abilities.objects.all()
    serializer_class = AbilitiesModelSerializer

