## Django

### Aula 1 => Criar ambiente

**1. Criar ambiente de virtual python:**

````sh
  python -m venv ./env_aula_01
````

**2. Ativar o ambiente virtual:**

````sh
  source ./env_aula_01/Scripts/activate
````

**3. Instalação do Django:**

````sh
  pip install django
````

**4. Guardar as dependências do projeto:**

````sh
  pip freeze > requirements.txt
````

### Aula 2 => Criar projeto

**1. Criar projeto Django (django-admin startproject NOMEDOPROJETO):**

````sh
  django-admin startproject projeto01
````

**2. Adicionar caminho da raíz de arquivos estáticos no projeto (arquivo ``settings.py``):**

````py
  STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
````

**3. Adicionar caminho dos templates no projeto (arquivo ``settings.py``):**

````py
  ...
  import os
  ...
  TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        ...
    }
  ]
  ...
````

**4. Entrar na pasta do projeto e iniciar o projeto com o comando:**

````sh
  python manage.py runserver
````

**5. Desativar o ambiente virtual:**

````sh
  deactivate
````

### Aula 3 => Configurar arquitetura MVP no projeto (Views)

**1. Criar um aplicativo dentro do projeto (python manage.py startapp NOMEDOAPP):**

````sh
  python manage.py startapp app01
````

**2. Criar pasta templates dentro do aplicativo:**

````sh
  cd ./app01 && mkdir templates && cd ..
````

**3. Criar arquivo de rotas no app: ``urls.py``**

**4. Incluir caminho das rotas do aplicativo no projeto (arquivo ``urls.py`` do projeto):**

````py
  ...
  from django.urls import path, include
  
  urlpatterns = [
    path('/', include('app01.urls')),
    path('admin/', admin.site.urls),
  ]
  ...
````

**5. Incluir caminho das views no app (arquivo ``urls.py`` do app):**

````py
  from django.urls import path

  from .views import index

  urlpatterns = [
    path('', index, name='index'),
  ]
````

**6. Criar função index das views (arquivo ``views.py`` do app):**

````py
  ...
  from django.http import HttpResponse

  def index(request):
    return HttpResponse('Hello World!')
````

### Aula 4 => Configurar arquitetura MVP no projeto (Models)

**1. Criação do model User no app (arquivo ``models.py``:**

````py
  ...
  class User(models.Model):
    nome = models.CharField('nome', max_length=30)
    telefone = models.IntegerField('telefone')
    email = models.CharField('email', max_length=30)
    
    def __str__(self):
      return f"Nome: {self.nome}, Telefone: {self.telefone}, Email: {self.email}"

````

**2. Registrar o app no projeto para ser possível criar as migrations (arquivo ``settings.py``:**

````py
  ...
  INSTALLED_APPS = [
    ...
    'app01'
  ]
  ...
````

**3. Criar as migrations:**

````sh
  python manage.py makemigrations
````

**4. Criar as tabelas no banco de dados a partir dos models:**

````sh
  python manage.py migrate
````

### Aula 5 => Configurar arquitetura MVP no projeto (Área administrativa)

**1. Ativar o Python shell para manipular os models da aplicação:**

````sh
  python manage.py shell
````

**2. Cadastrar um valor no model existente através do shell com os comandos:**

````py
  >>>> from app01.models import User
  >>>> 
  >>>> User.objects.all()
  <QuerySet []>
  >>>> 
  >>>> user = User(nome='Kamila', telefone='11111111', email='kamila@teste.com')
  >>>> user.save()
  >>>> user.id
  1
  >>>> user.nome
  'Kamila'
  >>>> user2 = User(nome='João', telefone='22222222', email='joao@teste.com')
  >>>> user2.save()
  >>>> user2.id
  2
  >>>> User.objects.all()
  >>>> <QuerySet [<User: Nome: Kamila, Telefone: 11111111, Email: kamila@teste.com>, <User: Nome: João, Telefone: 22222222, Email: joao@teste.com>]>
  >>> exit()
````

**3. Criar um super usuário para a área administrativa:**

````sh
  python manage.py createsuperuser
````

**4. Acessar a área administrativa em /admin e logar com o super usuário:**

````sh
  python manage.py runserver
````

**5. Registrar o model no admin do app para que seja possível manipular a tabela pelo admin (arquivo ``admin.py``):**

````py
  ...
  from .models import User

  admin.site.register(User)
````

## Templates e forms no Django

### Aula 1 => Criação de templates

**1. Alterar campo telefone no model para permitir números grandes (arquivo ``models.py``):**

````py
  ...
  telefone = models.BigIntegerField('telefone')
  ...
````

**2. Criar uma nova migration:**

````sh
  python manage.py makemigrations
````

**3. Atualizar as tabelas no banco de dados a partir dos models:**

````sh
  python manage.py migrate
````

**4. Criar template de usuário:**

````sh
  cd app01/templates/ && mkdir user && cd user && touch index.html
````

**5. Alterar o arquivo views para renderizar o html (arquivo ``views.py``):**

````py
  from django.shortcuts import render

  def index(request):
    return render(request, 'user/index.html')
````

**6. Criar rota para criar usuário:**

````sh
  touch criar.html
````

**7. Alterar o arquivo views para renderizar o html de criar usuário (arquivo ``views.py``):**

````py
  ...
  def create(request):
    return render(request, 'user/criar.html')
````

**8. Adicionar a rota de criar usuário nas rotas do app (arquivo ``urls.py``):**

````py
  ...
  urlpatterns = [
    path('', index, name='index'),
    path('criar/', create, name='criar'),
  ]
````

### Aula 2 => Criação de forms

**1. Criar arquivo forms no app:**

````sh
  cd app01 && touch forms.py
````

**2. Criar model form de user (arquivo ``forms.py``):**

````py
  from django import forms
  from .models import User

  # modelForm
  class UserForm(forms.ModelForm):
    class Meta:
      model = User
      fields = ['nome', 'telefone', 'email']
````

**3. Criar contexto de renderização de formulário na view (arquivo ``views.py``):**

````py
  ...
  from .forms import UserForm
  ...
  
  def create(request):
    if request.method == 'GET':
      form = UserForm()
      
      context = {
        'form': form
      }
    return render(request, 'user/criar.html', context=context)
````

**4. Criar arquivo base de template html:**

````sh
  cd app01/templates && touch base.html
````

**5. Adicionar [Jinja (engine de templates)](https://jinja.palletsprojects.com/en/3.1.x/) para adicionar código nos templates:**

  - **Alterar doctype no arquivo ``base.html`` de ``<!DOCTYPE html>`` para ``{% load static %}``**

  - **Criar pasta static no app, fazer o download dos arquivos [bootstrap](https://getbootstrap.com/docs/5.2/getting-started/download/) e adicionar as pastas css e js na pasta static:**

````sh
  cd app01 && mkdir static
````

  - **Importar bootstrap estático no arquivo base.html:**

````html
<link rel="stylesheet" type="text/css" href="{% static 'css/bootstrap.min.css' %}" />
````

  - **Adicionar title dinâmico no arquivo base.html:**

````html
<title>{% block title %} Capítulo de Django {% endblock %}</title>
````

  - **Adicionar conteúdo dinâmico no arquivo base.html:**

````html
<div>{% block content %}  {% endblock %}</div>
````

  - **Importar arquivos js no arquivo base.html:**

````html
<script
  src="https://code.jquery.com/jquery-3.6.1.slim.min.js"
  integrity="sha256-w8CvhFs7iHNVUtnSP0YKEg00p9Ih13rlL9zGqvLdePA="
  crossorigin="anonymous"
></script>
<script
  src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.10.2/dist/umd/popper.min.js"
  integrity="sha384-7+zCNj/IqJ95wo16oMtfsKbZ9ccEh31eOz1HGyDuCQ6wgnyJNSYdrPa03rtR1zdB"
  crossorigin="anonymous"
></script>
<script href="{% static 'js/bootstrap.min.js' %}"></script>
````

  - **Criar base de formulário com Jinja no arquivo ``criar.html``**
  
### Aula 3 => Criação de páginas dinâmicas

**1. Criar mais uma rota (arquivo ``urls.py``):**

````py
  ...
    path('modificar/<int:user_id>', modify, name='modificar'),
  ]
````

**2. Criar a view modify (arquivo ``views.py``):**

````py
  ...
  def modify(request, user_id):
    return render(request, 'user/index.html')
````

**3. Adicionar contexto na view modify para pegar id no template (arquivo ``views.py``):**

````py
  ...
  def modify(request, user_id):
    context = {
      'id': user_id
    }
    return render(request, 'user/index.html', context=context)
````