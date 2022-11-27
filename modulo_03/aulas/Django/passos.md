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

**5. Criar projeto Django (django-admin startproject NOMEDOPROJETO):**

````sh
  django-admin startproject projeto01
````

**6. Adicionar caminho da raíz de arquivos estáticos no projeto (arquivo ``settings.py``):**

````py
  STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
````

**7. Adicionar caminho dos templates no projeto (arquivo ``settings.py``):**

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

**8. Entrar na pasta do projeto e iniciar o projeto com o comando:**

````sh
  python manage.py runserver
````

**9. Desativar o ambiente virtual:**

````sh
  deactivate
````

### Aula 3 => Configurar arquitetura MVP no projeto (Views)

**10. Criar um aplicativo dentro do projeto (python manage.py startapp NOMEDOAPP):**

````sh
  python manage.py startapp app01
````

**11. Criar pasta templates dentro do aplicativo:**

````sh
  cd ./app01 && mkdir templates && cd ..
````

**12. Criar arquivo de rotas no app: ``urls.py``**

**13. Incluir caminho das rotas do aplicativo no projeto (arquivo ``urls.py`` do projeto):**

````py
  ...
  from django.urls import path, include
  
  urlpatterns = [
    path('/', include('app01.urls')),
    path('admin/', admin.site.urls),
  ]
  ...
````

**14. Incluir caminho das views no app (arquivo ``urls.py`` do app):**

````py
  from django.urls import path

  from .views import index

  urlpatterns = [
    path('', index, name='index'),
  ]
````

**15. Criar função index das views (arquivo ``views.py`` do app):**

````py
  ...
  from django.http import HttpResponse

  def index(request):
    return HttpResponse('Hello World!')
````

### Aula 4 => Configurar arquitetura MVP no projeto (Models)

**16. Criação do model User no app (arquivo ``models.py``:**

````py
  ...
  class User(models.Model):
    nome = models.CharField('nome', max_length=30)
    telefone = models.IntegerField('telefone')
    email = models.CharField('email', max_length=30)
    
    def __str__(self):
      return f"Nome: {self.nome}, Telefone: {self.telefone}, Email: {self.email}"

````

**17. Registrar o app no projeto para ser possível criar as migrations (arquivo ``settings.py``:**

````py
  ...
  INSTALLED_APPS = [
    ...
    'app01'
  ]
  ...
````

**18. Criar as migrations:**

````sh
  python manage.py makemigrations
````

**19. Criar as tabelas no banco de dados a partir dos models:**

````sh
  python manage.py migrate
````

### Aula 5 => Configurar arquitetura MVP no projeto (Área administrativa)

**20. Ativar o Python shell para manipular os models da aplicação:**

````sh
  python manage.py shell
````

**20. Cadastrar um valor no model existente através do shell com os comandos:**

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

**21. Criar um super usuário para a área administrativa:**

````sh
  python manage.py createsuperuser
````

**22. Acessar a área administrativa em /admin e logar com o super usuário:**

````sh
  python manage.py runserver
````

**23. Registrar o model no admin do app para que seja possível manipular a tabela pelo admin (arquivo ``admin.py``):**

````py
  ...
  from .models import User

  admin.site.register(User)
````