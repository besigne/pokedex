from rest_framework import routers
from core.view.pokemon_view import PokemonModelViewSet
from core.view.ability_view import AbilityModelViewSet
from core.view.evolution_view import EvolutionModelViewSet
from core.view.type_view import TypeModelViewSet
from django.urls import path

router = routers.SimpleRouter()
router.register(r'pokemons', PokemonModelViewSet, basename='pokemon')
router.register(r'abilities', AbilityModelViewSet, basename='ability')
router.register(r'types', TypeModelViewSet, basename='type')
router.register(r'evolutions', EvolutionModelViewSet, basename='evolution')

urlpatterns = router.urls
