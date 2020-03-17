from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse('Hello PokeCollector')

def about(request):
    return render(request, 'about.html')