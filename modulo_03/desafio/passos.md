````sh
# Criar ambiente virtual
python -m venv ./base

# Iniciar ambiente virtual
source ./base/Scripts/activate

# Instalar dependências
pip install -r requirements.txt

# Configurar tabelas no banco de dados
flask db init
flask db migrate
flask db upgrade

# Rodar a aplicação
flask --debug run
````
