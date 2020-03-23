from django.contrib import admin
from .models import Pokemon, Move, Feeding, Photo

# Register your models here.
admin.site.register(Pokemon)
admin.site.register(Move)
admin.site.register(Feeding)
admin.site.register(Photo)