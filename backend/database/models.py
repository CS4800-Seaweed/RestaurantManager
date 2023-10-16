from django.db import models

# Create your models here.
#TODO: ADD get_absolute_url() METHOD WHERE NECESSARY
class Restaurant(models.Model):
    restaurant_id = models.BigAutoField('restaurant id', primary_key=True)
    name = models.CharField('name', max_length=100)

    class Meta:
        verbose_name = 'restaurant'
        verbose_name_plural = 'restaurants'

    def __str__(self):
        return self.name

class Recipe(models.Model):
    recipe_id = models.BigAutoField('recipe id', primary_key=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, verbose_name='restaurant')
    instructions = models.CharField('instructions', max_length=5000)
    recipe_name = models.CharField('recipe name', max_length=100)

    #is it helpful for these to be ordered?
    #I remember chef saying it would be helpful to have a gui, so it WOULD be helpful to order these
    class Meta:
        indexes = [models.Index(fields=['recipe_name'])]
        ordering = ['-recipe_name']
        verbose_name = 'recipe'
        verbose_name_plural = 'recipes'

    def __str__(self):
        return self.recipe_name

#supplies are ordered by name
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
    supply_type = models.CharField(choices=SUPPLY_TYPE, max_length=20, verbose_name='supply type')

    class Meta:
        indexes = [models.Index(fields=['supply_name'])]
        ordering = ['-supply_name']
        verbose_name = 'supply'
        verbose_name_plural = 'supplies'

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

    class Meta:
        verbose_name = 'worker'
        verbose_name_plural = 'workers'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

#shipments are ordered by order date
class Shipment(models.Model):
    tracking_number = models.BigIntegerField('tracking number', primary_key=True)
    description = models.CharField('shipment description', max_length=500)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, verbose_name='restaurant')
    ordered = models.DateTimeField('order date')
    expected = models.DateTimeField('expected arrival')
    delivered = models.DateTimeField('recorded delivery')

    class Meta:
        indexes = [models.Index(fields=['ordered'])]
        ordering = ['-ordered']
        verbose_name = 'shipment'
        verbose_name_plural = 'shipments'

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
        verbose_name = 'recipe supply association'
        verbose_name_plural = 'recipe supply associations'

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
        verbose_name = 'active shipment supply association'
        verbose_name_plural = 'active shipment supply associations'