from django.db import models

# Create your models here.
class Pokemon(models.Model):
    name = models.CharField(max_length=20)
    e_type = models.CharField(max_length=20)
    description = models.TextField(max_length=250)
    generation = models.IntegerField()

    def __str__(self):
        return self.name

