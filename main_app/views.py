from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Pokemon
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def pokemon_index(request):
    pokemon = Pokemon.objects.all()
    return render(request, 'pokemon/index.html', { 'pokemon': pokemon })

def pokemon_detail(request, pokemon_id):
    pokemon = Pokemon.objects.get(id=pokemon_id)
    return render(request, 'pokemon/detail.html', {'pokemon': pokemon})

class PokemonCreate(CreateView):
    model = Pokemon
    fields = '__all__'
    success_url = '/pokemon/'

class PokemonUpdate(UpdateView):
    model = Pokemon
    fields = ['nickname', 'e_type', 'description', 'generation']

class PokemonDelete(DeleteView):
    model = Pokemon
    success_url = '/pokemon/'

