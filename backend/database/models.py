from django.db import models

# Create your models here.
#TODO: ADD EXPLICITLY NAMED FIELDS, get_absolute_url() METHOD, and Meta SUBCLASS WHERE NECESSARY
class Restaurant(models.Model):
    restaurant_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    recipe_id = models.BigAutoField(primary_key=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    instructions = models.CharField(max_length=5000)
    recipe_name = models.CharField(max_length=100)

    def __str__(self):
        return self.recipe_name

#TODO: CLARIFY IF THESE ARE INGREDIENTS OR NOT
class Supply(models.Model):
    supply_id = models.BigAutoField(primary_key=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    storage_location = models.CharField(max_length=20)
    quantity = models.IntegerField()
    quantity_units = models.CharField(max_length=20) #gallons vs liters vs pounds etc.
    resupply = models.BooleanField()
    supply_name = models.CharField(max_length=5000)

    def __str__(self):
        return self.supply_name

#TODO: CLARIFY WHETHER THIS BELONGS IN THE STOCKING/RESTOCKING DATABASE
class Worker(models.Model):
    username = models.CharField(max_length=70, primary_key=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=320)
    user_password = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Shipment(models.Model):
    tracking_number = models.BigIntegerField(primary_key=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    ordered = models.DateTimeField()
    expected = models.DateTimeField()
    delivered = models.DateTimeField()

    def __str__(self):
        return 'tracking_number'

#since this is a join table, it probably shouldn't have a str method, that'd be kinda weird
class RecipeSupply(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    supply = models.ForeignKey(Supply, on_delete=models.CASCADE)
    amount = models.FloatField()

    #join the recipe and supply as a joint primary key
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['recipe', 'supply'], name='unique_recipe_supply')
        ]

#Same as recipe supply, probably shouldnt have a str method
class ShipmentSupply(models.Model):
    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE)
    supply = models.ForeignKey(Supply, on_delete=models.CASCADE)
    amount = models.IntegerField()

    #join the shipment and supply as a joint primary key
    class Meta:
        constraints = [
            models.UniqueConstraint(fields = ['shipment', 'supply'], name='unique_shipment_supply')
        ]