## Introdução ao teste de software

### Aula 1 => Criar testes unitários com unittest

**1. Criar ambiente de virtual python:**

````sh
  python -m venv ./env_aula_01
````

**2. Ativar o ambiente virtual:**

````sh
  source ./env_aula_01/Scripts/activate
````

**3. Instalação do unittest:**

````sh
  pip install unittest2
````

**4. Criar arquivo de teste e classe com o primeiro teste:**

````sh
  touch test.py
````

````py
# test.py

import unittest
from root_square_solver import rootSquareSolver

class CheckRootSquareSolver(unittest.TestCase):
  def test_checkTwoRoots(self):
    response = rootSquareSolver(1, -5, 6) 
    self.assertEqual(len(response), 2)
````

**4. Rodar o primeiro teste:**

````sh
  python -m unittest -v test.py
````

**4. Criar arquivo com a função ``rootSquareSolver`` que calcula equações de 2º grau:**

````sh
  touch root_square_solver.py
````

**5. Criar novos testes com base nas [regras de cálculo da equação de 2º grau](https://brasilescola.uol.com.br/matematica/equacao-2-grau), e se não passarem, refatorar a função ``rootSquareSolver`` para que passem**

### Aula 2 => Criar testes de requisições (CRUD Flask)

**1. Instalar a lib de requisições:**

````sh
  pip install requests
````

**2. Criar arquivo ``test_api_flask.py`` e importar as libs requests e unittest:**

````sh
  touch test_api_flask.py
````

**3. Abrir outro terminal na pasta da aula de CRUD com Flask e deixar o projeto rodando:**

````sh
  source ./base/Scripts/activate
  flask --debug run
````

**4. Criar primeiro teste de Criação de usuário:**

````py
# test_api_flask.py

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
````

**5. Rodar os testes:**

````sh
  python -m unittest -v test_api_flask.py
````

## Testando projetos

### Aula 1 => Introdução à testes no Django

**1. Abir a aplicação de CRUD do Django**

**2. No arquivo ``test.py`` iniciar os primeiros testes:**

````py
from django.test import TestCase

def add_num(num):
  return num + 1
  
class SimpleTestCase(TestCase):
  def setUp(self):
    self.num = 1
    
  def test_add_num(self):
    value = add_num(self.num)
    self.assertTrue(value == 2)
````

**3. Rodar os testes:**

````sh
python manage.py test
````

### Aula 2 => Testes em models no Django

**1. Remover arquivo de testes ``tests.py`` da aplicação:**

````sh
cd app && rm -rf tests.py && cd ..
````

**2. Criar pasta tests com o arquivo inicial ``__init__.py`` e o arquivo ``test_models.py``:**

````sh
cd app && mkdir tests && cd tests &&  touch __init__.py test_models.py && cd ../..
````

**3. Instalar a lib coverage:**

````sh
pip install coverage
````

**4. Criar o arquivo ``.coveragerc`` na raíz do projeto:**

````sh
  touch .coveragerc
````

**5. Adicionar configurações no arquivo ``.coveragerc`` para indicar a cobertura de arquivos que serão testados ou omitidos:**

````coveragerc
[run]
source = .
  
omit = 
    */__init__.py
    */settings.py
    */manage.py
    */wsgi.py
    */asgi.py
    */apps.py
    */urls.py
    */admin.py
    */migrations/*
    */tests/*
````

**6. Rodar os testes:**

````sh
coverage run manage.py test
````

**7. Ver o relatório da cobertura de testes:**

````sh
coverage report
````

**8. Ver o relatório da cobertura em html:**

````sh
coverage html
cd htmlcov
python -m http.server
cd ..
````

**9. Criar testes nos models no arquivo ``test_models.py``:**

````py
from django.test import TestCase
from app.models import User

class SampleTestCase(TestCase):
  def setUp(self):
    user = User(nome="Kamila",telefone=11111111,email="kamila@test.com")
    self.user = user
    
  def test_str(self):
    self.assertEquals(str(self.user), "Nome: Kamila, Telefone: 11111111, Email: kamila@test.com")
````

**10. Rodar novamente os testes e verificar a cobertura:**

````sh
# rodar testes
coverage run manage.py test

# Verificar cobertura
coverage report

# OU

coverage html
cd htmlcov
python -m http.server
cd ..
````

### Aula 4 => Testes em views no Django

**1. Criar arquivo de testes de views na pasta tests ``test_views.py``:**

````sh
cd app/tests && touch test_views.py && cd ../..
````

**2. Criar teste para a rota index no arquivo ``test_views.py``:**

````py
from django.test import TestCase, Client
from django.urls import reverse_lazy

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
````

**3. Rodar os testes e verificar a cobertura:**

````sh
# rodar testes
coverage run manage.py test

# Verificar cobertura
coverage report
````

**4. Criar teste para a rota create no arquivo ``test_views.py``:**

````py
...
  def test_create(self):
    request = self.client.post(reverse_lazy('create'), data=self.user_data)
    self.assertEquals(request.status_code, 302)
````

**5. Rodar os testes e verificar a cobertura:**

````sh
# rodar testes
coverage run manage.py test

# Verificar cobertura
coverage report
````