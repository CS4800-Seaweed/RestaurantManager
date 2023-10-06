from django.test import TestCase
from models import Worker

# Create your tests here.
class login_test(TestCase):
    def test_user_model(self):
        obj = Worker.objects.create(username="testuser123")
    
        self.assertEqual(obj.username, "testuser123")