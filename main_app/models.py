from django.db import models
from django.urls import reverse

# Create your models here.

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner'),
)

class Pokemon(models.Model):
    name = models.CharField(max_length=20)
    nickname = models.CharField(max_length=20)
    e_type = models.CharField(max_length=20)
    description = models.TextField(max_length=250)
    generation = models.IntegerField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'pokemon_id': self.id})

class Feeding(models.Model):
    date = models.DateField()
    meal = models.CharField(
        max_length=1,
        choices=MEALS,
        default=MEALS[0][0],
    )

    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.get_meal_display()} on {self.date}'

class Move(models.Model):
    name: models.CharField(max_length=20)
    m_type: models.CharField(max_length=20)
    
    def __str__(self):
        return self.name