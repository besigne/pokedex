import json
import requests
from rest_framework import serializers
from django.http import JsonResponse


def pokefinder(pokemon_finder):

    url = 'https://pokeapi.co/api/v2/pokemon/' + pokemon_finder + '/'
    pokemon = requests.get(url=url)
    data = json.loads(pokemon.text)

    if pokemon.status_code == 200:
        return data
    else:
        return JsonResponse({"error": "Request failed"}, status=pokemon.status_code)


class PokemonModelSerializer(serializers.ModelSerializer):
    brute_pokemon = pokefinder(pokemon_finder='25')
