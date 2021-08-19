from rest_framework.viewsets import ModelViewSet
from core.models.pokemons import Pokemons
from core.serializers.pokemons import PokemonsModelSerializer


class PokemonsModelViewSet(ModelViewSet):

    queryset = Pokemons.objects.all()
    serializer_class = PokemonsModelSerializer

