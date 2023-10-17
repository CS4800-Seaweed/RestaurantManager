from django.db import models

# Create your models here.
class Company(models.Model):
    restaurant_id = models.BigAutoField('company id', primary_key=True)
    name = models.CharField('name', max_length=100)

    class Meta:
        verbose_name = 'company'
        verbose_name_plural = 'companies'

    def __str__(self):
        return self.name

class Worker(models.Model):
    username = models.CharField('username', max_length=70, primary_key=True)
    restaurant = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='restaurant')
    first_name = models.CharField('first name', max_length=50)
    last_name = models.CharField('last name', max_length=50)
    email = models.CharField('email', max_length=320)
    user_password = models.CharField('password', max_length=50)

    class Meta:
        verbose_name = 'worker'
        verbose_name_plural = 'workers'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'