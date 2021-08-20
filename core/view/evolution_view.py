from rest_framework.viewsets import ModelViewSet
from core.model.evolution import Evolution
from core.serializer.evolution_serializer import EvolutionModelSerializer


class EvolutionModelViewSet(ModelViewSet):
    queryset = Evolution.objects.all()
    serializer_class = EvolutionModelSerializer
