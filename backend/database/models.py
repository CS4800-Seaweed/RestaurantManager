from django.db import models

# Create your models here.
class Restaurants(models.Model):
    id = models.BigAutoField(primary_key=True)

class Restaurant(models.Model):
    restaurant_id = models.BigAutoField(primary_key=True)
    restaurants = models.ForeignKey(Restaurants, on_delete=models.CASCADE)

class Recipe(models.Model):
    recipe_id = models.BigAutoField(primary_key=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    instructions = models.CharField(max_length=5000)

class Supply(models.Model):
    supply_id = models.BigAutoField(primary_key=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    storage_location = models.CharField(max_length=20)
    quantity = models.IntegerField()
    resupply = models.BooleanField()

class Worker(models.Model):
    username = models.CharField(max_length=70, primary_key=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=320)
    user_password = models.CharField(max_length=50)

class Shipment(models.Model):
    tracking_number = models.BigIntegerField(primary_key=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    ordered = models.DateTimeField()
    expected = models.DateTimeField()
    delivered = models.DateTimeField()

class RecipeSupply(models.Model):
    recipe_supply_id = models.BigAutoField(primary_key=True)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    supply = models.ForeignKey(Supply, on_delete=models.CASCADE)
    amount = models.FloatField()

class ShipmentSupply(models.Model):
    shipment_supply_id = models.BigAutoField(primary_key=True)
    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE)
    supply = models.ForeignKey(Supply, on_delete=models.CASCADE)
    amount = models.IntegerField()