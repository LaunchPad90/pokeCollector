from django.shortcuts import render
from django.http import HttpResponse
# from .models import Pokemon, pokemon
# Create your views here.

class Pokemon:
    def __init__(self, name, e_type, description, generation):
        self.name = name
        self.e_type = e_type
        self.description = description
        self.generation = generation

pokemon = [
    Pokemon('Pikachu', 'Electric', 'Hates pokeballs, cute as a button', 1),
    Pokemon('Squirtle', 'Water', 'Hard shell', 1),
    Pokemon('Charmander', 'Fire', 'Dragon looking', 1)
]

def home(request):
    return HttpResponse('Hello PokeCollector')

def about(request):
    return render(request, 'about.html')

def pokemon_index(request):
    return render(request, 'pokemon/index.html', { 'pokemon': pokemon })