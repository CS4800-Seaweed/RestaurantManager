from django.db import models

# Create your models here.
#TODO: ADD get_absolute_url() METHOD, AND Meta SUBCLASS WHERE NECESSARY
class Restaurant(models.Model):
    restaurant_id = models.BigAutoField('restaurant id', primary_key=True)
    name = models.CharField('name', max_length=100)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    recipe_id = models.BigAutoField('recipe id', primary_key=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, verbose_name='restaurant')
    instructions = models.CharField('instructions', max_length=5000)
    recipe_name = models.CharField('recipe name', max_length=100)

    def __str__(self):
        return self.recipe_name

class Supply(models.Model):
    SUPPLY_TYPE = (
        ('INGREDIENT', 'used as an ingredient'),
        ('MATERIAL', 'not used as an ingredient')
    )

    supply_id = models.BigAutoField('supply id', primary_key=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, verbose_name='restaurant')
    storage_location = models.CharField('storage location', max_length=20)
    quantity = models.IntegerField('quantity')
    quantity_units = models.CharField('units', max_length=20) #gallons vs liters vs pounds etc.
    resupply = models.BooleanField('in stock')
    supply_name = models.CharField('supply name', max_length=5000)

    def __str__(self):
        return self.supply_name

#TODO: CLARIFY WHETHER THIS BELONGS IN THE STOCKING/RESTOCKING DATABASE
class Worker(models.Model):
    username = models.CharField('username', max_length=70, primary_key=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, verbose_name='restaurant')
    first_name = models.CharField('first name', max_length=50)
    last_name = models.CharField('last name', max_length=50)
    email = models.CharField('email', max_length=320)
    user_password = models.CharField('password', max_length=50)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Shipment(models.Model):
    tracking_number = models.BigIntegerField('tracking number', primary_key=True)
    description = models.CharField('shipment description', max_length=500)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, verbose_name='restaurant')
    ordered = models.DateTimeField('order date')
    expected = models.DateTimeField('expected arrival')
    delivered = models.DateTimeField('recorded delivery')

    def __str__(self):
        return self.tracking_number

#since this is a join table, it probably shouldn't have a str method, that'd be kinda weird
class RecipeSupply(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, verbose_name='recipe id')
    supply = models.ForeignKey(Supply, on_delete=models.CASCADE, verbose_name='supply id')
    amount = models.FloatField('amount')

    #join the recipe and supply as a joint primary key
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['recipe', 'supply'], name='unique_recipe_supply')
        ]

#Same as recipe supply, probably shouldnt have a str method
class ShipmentSupply(models.Model):
    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE, verbose_name='shipment number')
    supply = models.ForeignKey(Supply, on_delete=models.CASCADE, verbose_name='supply id')
    amount = models.IntegerField('amount')

    #join the shipment and supply as a joint primary key
    class Meta:
        constraints = [
            models.UniqueConstraint(fields = ['shipment', 'supply'], name='unique_shipment_supply')
        ]