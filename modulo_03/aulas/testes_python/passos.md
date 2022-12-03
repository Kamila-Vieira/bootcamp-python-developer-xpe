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

### Aula 1 => Criar testes de requisições (CRUD Flask)

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