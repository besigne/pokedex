from rest_framework import routers
from core.view.pokemon_view import PokemonsModelViewSet
from core.view.ability_view import AbilitiesModelViewSet
from core.view.evolution_view import EvolutionsModelViewSet
from django.urls import path

router = routers.SimpleRouter()
router.register(r'pokemons', PokemonsModelViewSet, basename='pokemon')
router.register(r'abilities', AbilitiesModelViewSet, basename='ability')
router.register(r'evolutions', EvolutionsModelViewSet, basename='evolution')
urlpatterns = [
] + router.urls
