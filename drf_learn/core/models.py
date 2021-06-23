from django.db import models

# Create your models here.

class MissedIngredients(models.Model):
    ids = models.IntegerField()
    amount = models.FloatField()
    unit = models.CharField(max_length=20)
    name = models.CharField(max_length=25)
    image = models.TextField()