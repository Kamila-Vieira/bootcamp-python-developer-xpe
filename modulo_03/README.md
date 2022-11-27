### Preparação do ambiente virtual python: 

Ambiente virtual de desenvolvimento python no VSCode.

1. Verificar versão do python (v3.x.x):

````sh
  python --version
````

2. Criar ambiente de virtual python (python -m venv ./NOMEDOAMBIENTE):

````sh
  python -m venv ./env
````

3. Ativar o ambiente virtual: 

Linux/Mac: ``source ./env/bin/activate``
Windows: ``source ./env/Scripts/activate``

4. Instalação de pacotes (exemplo Django):

````sh
  pip install django
````

5. Verificar a versão do pacote instalado (exemplo Django):

````sh
  python -m django --version
````

6. Guardar as dependências do projeto:

````sh
  pip freeze > requirements.txt
````

7. Desativar o ambiente virtual:

````sh
  deactivate
````

Obs.: É possível adicionar um novo pacote no arquivo requirements.txt e rodar o comando ``pip install -r requirements.txt``, para instalar varias dependências de uma vez.

### Plano de ensino Módulo 3: Python para aplicações web

#### Capítulo 1. Introdução aos sistemas web

1.1 Introdução

1.2 Como funcionam os sistemas web

1.3 Fluxo de dados

1.4 Arquitetura

1.5. APIs

#### Capítulo 2. HTML

2.1 Introdução

2.2 Prática com HTML - parte 1

2.3 Prática com HTML - parte 2

2.4 Prática com HTML - parte 3

2.5. Prática com HTML - parte 4

#### Capítulo 3. CSS

3.1 Introdução

3.2 Prática com CSS - parte 1

3.3 Prática com CSS - parte 2

3.4 Prática com CSS - parte 3

3.5. Prática com CSS - parte 4

#### Capítulo 4. Eventos

4.1 Introdução

4.2 Prática com Eventos

#### Capítulo 5. Django

5.1. Preparação do ambiente

5.2. Criação e configuração do primeiro projeto

5.3 Arquitetura MVP

5.4. Models

5.5. Área administrativa 

#### Capítulo 6. Templates e forms no Django

6.1. Criação de templates 

6.2. Criação de forms

6.3. Criação de páginas dinâmicas

#### Atividade Prática