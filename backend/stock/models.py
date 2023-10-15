from django.db import models

#TODO: MIGRATE THE MODELS FROM THE DATABASE CLASS HERE
class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField(default=0)
    unit = models.CharField(max_length=50)

class RestockRecord(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    added_quantity = models.PositiveIntegerField()
    date_restocked = models.DateTimeField(auto_now_add=True)

