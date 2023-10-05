from django.test import TestCase
from .models import models
# Create your tests here.

class ModelTestCase(TestCase):
    def setUp(self):
        models.objects.create(name="TestCase")
        
    def test1(self):
        obj = models.objects.get(name="TestCase")
        self.assertEqual(obj.name, 'TestCase')