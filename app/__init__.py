# app/__init__.py
from flask import Flask

app = Flask(__name__)

# Configuração do banco de dados MySQL
app.config['DB_CONFIG'] = {
    'host': 'localhost',  # Alterar se necessário
    'user': 'root',       # Usuário do MySQL
    'password': 'a14s2e82',   # Senha do MySQL
    'database': 'pessoaDB' # Nome do banco de dados
}

from app.routes import routes