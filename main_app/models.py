from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

from datetime import date

# Create your models here.

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner'),
)

class Move(models.Model):
    name = models.CharField(max_length=20)
    m_type = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('/moves/', kwargs={'pk': self.id})
    

class Pokemon(models.Model):
    name = models.CharField(max_length=20)
    nickname = models.CharField(max_length=20)
    e_type = models.CharField(max_length=20)
    description = models.TextField(max_length=250)
    generation = models.IntegerField()
    moves = models.ManyToManyField(Move)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'pokemon_id': self.id})

    def fed_for_today(self):
        return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)

class Feeding(models.Model):
    date = models.DateField('feeding date')
    meal = models.CharField(
        max_length=1,
        choices=MEALS,
        default=MEALS[0][0],
    )

    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.get_meal_display()} on {self.date}'

    class Meta:
        ordering = ['-date']

class Photo(models.Model):
    url = models.CharField(max_length=200)
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for poke_id: {self.pokemon_id} @{self.url}"