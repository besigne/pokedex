from rest_framework.viewsets import ModelViewSet

from core.models import Pokemons, Abilities
from core.serializers import PokemonsModelSerializer, AbilitiesModelSerializer


class PokemonsModelViewSet(ModelViewSet):
    queryset = Pokemons.objects.all()
    serializer_class = PokemonsModelSerializer


class AbilitiesModelViewSet(ModelViewSet):
    queryset = Abilities.objects.all()
    serializer_class = AbilitiesModelSerializer
