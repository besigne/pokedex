from rest_framework import routers
from core import views

router = routers.SimpleRouter()
router.register(r'pokemons', views.PokemonsModelViewSet, basename='pokemon')
router.register(r'abilities', views.AbilitiesModelViewSet, basename='ability')

urlpatterns = [
] + router.urls
