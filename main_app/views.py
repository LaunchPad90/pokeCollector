from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from .models import Pokemon, Move, Feeding
from .forms import FeedingForm
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
    moves_pokemon_doesnt_have = Move.objects.exclude(id__in = pokemon.moves.all().values_list('id'))
    feeding_form = FeedingForm()
    return render(request, 'pokemon/detail.html', {
        'pokemon': pokemon,
        'feeding_form': feeding_form,
        'moves': moves_pokemon_doesnt_have
    })

def add_feeding(request, pokemon_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.pokemon_id = pokemon_id
        new_feeding.save()
    return redirect('detail', pokemon_id=pokemon_id)

def moves_list(request, move_id):
    Move.objects.all()
    return render(request, 'moves/moves_list.html', {'moves_list': moves_list})

def assoc_move(request, pokemon_id, move_id):
    Pokemon.objects.get(id=pokemon_id).moves.add(move_id)
    return redirect('detail', pokemon_id=pokemon_id)

def unassoc_move(request, pokemon_id, move_id):
    Pokemon.objects.get(id=pokemon_id).moves.remove(move_id)
    return redirect('detail', pokemon_id=pokemon_id)

class PokemonCreate(CreateView):
    model = Pokemon
    fields = ['name', 'nickname', 'e_type', 'description', 'generation']


class PokemonUpdate(UpdateView):
    model = Pokemon
    fields = ['nickname', 'e_type', 'description', 'generation']

class PokemonDelete(DeleteView):
    model = Pokemon
    success_url = '/pokemon/'

class MoveList(ListView):
    model = Move
    
class MoveDetail(DetailView):
    model = Move    

class MoveCreate(CreateView):
    model = Move
    fields = '__all__'
    
class MoveUpdate(UpdateView):
    model = Move
    fields = '__all__'

class MoveDelete(DeleteView):
    model = Move
    success_url = '/moves/'