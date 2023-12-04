from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.
class Company(models.Model):
    company_id = models.BigAutoField('company id', primary_key=True)
    name = models.CharField('name', max_length=100)

    class Meta:
        verbose_name = 'company'
        verbose_name_plural = 'companies'

    def __str__(self):
        return self.name
    
class WorkerManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, email, password, **extra_fields)

class Worker(AbstractBaseUser, PermissionsMixin):
    username = models.CharField('username', max_length=70, primary_key=True)
    restaurant = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='restaurant')
    first_name = models.CharField('first name', max_length=50)
    last_name = models.CharField('last name', max_length=50)
    email = models.CharField('email', max_length=320)
    #user_password = models.CharField('password', max_length=50)

    objects = WorkerManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'password']

    #set permissions mixin
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)



    class Meta:
        verbose_name = 'worker'
        verbose_name_plural = 'workers'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
