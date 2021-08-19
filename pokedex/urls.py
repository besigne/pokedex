from rest_framework import routers
from core.views.pokemons import PokemonsModelViewSet
from core.views.abilities import AbilitiesModelViewSet
from core.views.evolutions import EvolutionsModelViewSet
from django.urls import path

router = routers.SimpleRouter()
router.register(r'pokemons', PokemonsModelViewSet, basename='pokemon')
router.register(r'abilities', AbilitiesModelViewSet, basename='ability')
router.register(r'evolutions', EvolutionsModelViewSet, basename='evolution')

urlpatterns = [
] + router.urls
