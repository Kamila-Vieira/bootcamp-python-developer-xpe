## Flask

### Aula 1 => Criar ambiente

**1. Criar ambiente de virtual python:**

````sh
  python -m venv ./base
````

**2. Ativar o ambiente virtual:**

````sh
  source ./base/Scripts/activate
````

**3. Instalação do Flask:**

````sh
  pip install flask
  python -m flask --version
````

**4. Guardar as dependências do projeto:**

````sh
  pip freeze > requirements.txt
````

**5. Desativar o ambiente virtual:**

````sh
  deactivate
````

### Aula 2 => Criar projeto

**1. Criar arquivo ``app.py``:**

````sh
  touch app.py
````

**2. Fazer configurações iniciais do Flask no arquivo ``app.py``:**

````py
  from flask import Flask

  app = Flask(__name__)

  @app.route('/')
  def index():
    return '<h1>Hello World!</h1>'
````

**3. Definir arquivo de entrada do app:**

````sh
 set FLASK_APP = app.py
````

**4. Rodar o servidor:**

````sh
  flask run
````

**Obs.: Para ativar o hot reload basta adicionar a flag ``--debug``:**

````sh
  flask --debug run
````

### Aula 3 => Criação de templates 

**1. Criar pasta templates dentro do aplicativo com o arquivo html inicial:**

````sh
  mkdir templates && cd templates && touch index.html && cd ..
````

**2. Adicionar caminho da pasta templates no projeto (arquivo ``app.py``):**

````py
  import os
  from flask import Flask, render_template

  template_dir = os.path.abspath('./templates')

  app = Flask(__name__, template_folder=template_dir)

  @app.route('/')
  def index():
    return render_template('index.html')
````

**3. Adicionar rotas dinâmicas com query params (arquivo ``app.py``):**

````py
  ...
  @app.route('/user')
  @app.route('/user/<name>')
  def user(name=None):
    return render_template('index.html', name=name)
````

### Aula 4 => Flask - Forms

**1. Instalar flask-wtf e atualizar as dependências do projeto:**

````sh
  pip install flask-wtf
  pip freeze > requirements.txt
````

**2. Criar arquivo de forms:**

````sh
  touch forms.py
````

**3. Configurar o arquivo form:**

````py
  from flask_wtf import FlaskForm
  from wtforms import StringField, SubmitField
  from wtforms.validators import DataRequired

  class NameForm(FlaskForm):
    name = StringField('Qual é o seu nome?', validators=[DataRequired()])
    submit = SubmitField('Enviar')
````

**4. Alterar app para renderizar o formulário:**

````py
  ...
  from form import NameForm 

  ...

  app.config['SECRET_KEY'] = 'AFASFAOJkkljfasf~ç3219-0fm'

  @app.route('/', methods = ['GET', 'POST'])
  def index():
    name = None
    form = NameForm()
    
    if form.validate_on_submit():
      name = form.name.data
      form.name.data = ''
      
    return render_template('index.html', name = name, form = form)
````
