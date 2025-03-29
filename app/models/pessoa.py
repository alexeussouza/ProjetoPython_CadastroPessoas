# app/models.py
import mysql.connector
from app import app

class Pessoa:
    def __init__(self, id, nome, telefone, email):
        self.id = id
        self.nome = nome
        self.telefone = telefone
        self.email = email

# Função para conectar ao banco de dados
def get_db_connection():
    return mysql.connector.connect(**app.config['DB_CONFIG'])
