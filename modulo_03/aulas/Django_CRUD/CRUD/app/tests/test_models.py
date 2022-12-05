from django.test import TestCase
from app.models import User

class SampleTestCase(TestCase):
  def setUp(self):
    user = User(nome="Kamila",telefone=11111111,email="kamila@test.com")
    self.user = user
    
  def test_str(self):
    self.assertEquals(str(self.user), "Nome: Kamila, Telefone: 11111111, Email: kamila@test.com")