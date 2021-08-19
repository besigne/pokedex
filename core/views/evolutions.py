from rest_framework.viewsets import ModelViewSet
from core.models.evolutions import Evolutions
from core.serializers.evolutions import EvolutionModelSerializer


class EvolutionsModelViewSet(ModelViewSet):
    queryset = Evolutions.objects.all()
    serializer_class = EvolutionModelSerializer
