from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm

import uuid
import boto3

from .models import Pokemon, Move, Feeding, Photo
from .forms import FeedingForm

S3_BASE_URL = 'https://s3-us-west-2.amazonaws.com/'
BUCKET = 'catcollector1234'
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def pokemon_index(request):
    pokemon = Pokemon.objects.all()
    return render(request, 'pokemon/index.html', { 'pokemon': pokemon })

@login_required
def pokemon_detail(request, pokemon_id):
    pokemon = Pokemon.objects.get(id=pokemon_id)
    moves_pokemon_doesnt_have = Move.objects.exclude(id__in = pokemon.moves.all().values_list('id'))
    feeding_form = FeedingForm()
    return render(request, 'pokemon/detail.html', {
        'pokemon': pokemon,
        'feeding_form': feeding_form,
        'moves': moves_pokemon_doesnt_have
    })

@login_required
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

@login_required
def add_photo(request, pokemon_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            photo = Photo(url=url, pokemon_id=pokemon_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', pokemon_id=pokemon_id)

@login_required
def assoc_move(request, pokemon_id, move_id):
    Pokemon.objects.get(id=pokemon_id).moves.add(move_id)
    return redirect('detail', pokemon_id=pokemon_id)

@login_required
def unassoc_move(request, pokemon_id, move_id):
    Pokemon.objects.get(id=pokemon_id).moves.remove(move_id)
    return redirect('detail', pokemon_id=pokemon_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

class PokemonCreate(LoginRequiredMixin, CreateView):
    model = Pokemon
    fields = ['name', 'nickname', 'e_type', 'description', 'generation']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PokemonUpdate(LoginRequiredMixin, UpdateView):
    model = Pokemon
    fields = ['nickname', 'e_type', 'description', 'generation']

class PokemonDelete(LoginRequiredMixin, DeleteView):
    model = Pokemon
    success_url = '/pokemon/'

class MoveList(ListView):
    model = Move
    
class MoveDetail(DetailView):
    model = Move    

class MoveCreate(LoginRequiredMixin, CreateView):
    model = Move
    fields = '__all__'
    
class MoveUpdate(LoginRequiredMixin, UpdateView):
    model = Move
    fields = '__all__'

class MoveDelete(LoginRequiredMixin, DeleteView):
    model = Move
    success_url = '/moves/'