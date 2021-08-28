from django.test import TestCase

from core.model.ability import Ability
from core.model.evolution import Evolution
from core.model.pokemon import Pokemon


class AbilityTestCase(TestCase):
    def setUp(self):
        Ability.objects.create(name="AbilityTest", description="description test")


class EvolutionTestCase(TestCase):
    def setUp(self):
        Evolution.objects.create(name="Pokemon Test Evolution")


class PokemonTestCase(TestCase):
    def setUp(self):
        print('Testing if we can create a pokemon without evolution')
        Pokemon.objects.create(name="Pokemon Test", type=[], Ability=[])


