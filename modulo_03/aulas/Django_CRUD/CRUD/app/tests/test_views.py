from django.test import TestCase, Client
from django.urls import reverse_lazy
from app.models import User

class SampleTestCase(TestCase):
  def setUp(self):
    self.user_data = {
      'nome': 'Kamila',
      'telefone':11111111,
      'email':"kamila@test.com"
    }
    self.client = Client()
    
  def test_index(self):
    request = self.client.get(reverse_lazy('index'))
    self.assertEquals(request.status_code, 200)
    
  def test_create(self):
    request = self.client.post(reverse_lazy('create'), data=self.user_data)
    self.assertEquals(request.status_code, 302)