from rest_framework.viewsets import ModelViewSet
from core.model.pokemon import Pokemon
from core.serializer.pokemon_serializer import PokemonModelSerializer


class PokemonModelViewSet(ModelViewSet):

    queryset = Pokemon.objects.all()
    serializer_class = PokemonModelSerializer

