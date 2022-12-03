import requests 
import unittest
import json

class TestAPI(unittest.TestCase):
  
  def test_createUser(self):
    url = 'http://127.0.0.1:5000/users/create'
    payload = {
      "name": "Kamila",
      "age": "24",
      "address": "Rua A"
    }
    headers = {'Content-Type': "application/json"}
    response = requests.request('POST', url=url, headers=headers,data=json.dumps(payload))
    data = response.json()[0]
    
    self.assertEqual(payload['name'], data['name'])
    self.assertEqual(payload['age'], data['age'])
    self.assertEqual(payload['address'], data['address'])
    
    userId = data['id']
    
    url = f'http://127.0.0.1:5000/users/update/{userId}'
    
    payload = {
      "name": "Kamila Almeida",
      "age": "24",
      "address": "Rua A"
    }
    
    response = requests.request('PUT', url=url, headers=headers,data=json.dumps(payload))
    data = response.json()[0]
    
    self.assertEqual(payload['name'], data['name'])
    