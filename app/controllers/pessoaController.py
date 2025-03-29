# app/controllers.py
from app.models.pessoa import get_db_connection, Pessoa

def adicionar_pessoa(nome, telefone, email):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO pessoas (nome, telefone, email) VALUES (%s, %s, %s)", (nome, telefone, email))
    conn.commit()
    cursor.close()
    conn.close()

def listar_pessoas(page=1, per_page=5):
    conn = get_db_connection()
    cursor = conn.cursor()

    # Calcula o índice inicial do primeiro registro a ser exibido
    offset = (page - 1) * per_page

    # Busca os registros paginados
    cursor.execute("SELECT id, nome, telefone, email FROM pessoas LIMIT %s OFFSET %s", (per_page, offset))
    pessoas = [Pessoa(id, nome, telefone, email) for id, nome, telefone, email in cursor.fetchall()]

    # Conta o total de registros para calcular o número de páginas
    cursor.execute("SELECT COUNT(*) FROM pessoas")
    total_registros = cursor.fetchone()[0]
    cursor.close()
    conn.close()

    # Calcula o total de páginas
    total_paginas = (total_registros + per_page - 1) // per_page

    return pessoas, total_paginas


def alterar_pessoa(id, nome, telefone, email):
    """ Atualiza os dados de uma pessoa pelo ID """
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE pessoas SET nome=%s, telefone=%s, email=%s WHERE id=%s", (nome, telefone, email, id))
    conn.commit()
    cursor.close()
    conn.close()

def excluir_pessoa(id):
    """ Remove uma pessoa do banco de dados pelo ID """
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM pessoas WHERE id=%s", (id,))
    conn.commit()
    cursor.close()
    conn.close()

