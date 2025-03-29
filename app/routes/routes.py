# app/routes.py
from flask import render_template, request, redirect, url_for
from app import app
from app.controllers.pessoaController import adicionar_pessoa, listar_pessoas, alterar_pessoa, excluir_pessoa


@app.route('/')
@app.route('/<int:page>')
def index(page=1):
    # página recebe um número (page) e passa para listar_pessoas().
    pessoas, total_paginas = listar_pessoas(page) 
    return render_template('index.html', pessoas=pessoas, page=page, total_paginas=total_paginas)

@app.route('/adicionar', methods=['POST'])
def adicionar():
    nome = request.form['nome']
    telefone = request.form['telefone']
    email = request.form['email']
    adicionar_pessoa(nome, telefone, email)
    return redirect(url_for('index'))

@app.route('/alterar/<int:id>', methods=['POST'])
def alterar(id):
    nome = request.form['nome']
    telefone = request.form['telefone']
    email = request.form['email']
    alterar_pessoa(id, nome, telefone, email)
    return redirect(url_for('index'))

@app.route('/excluir/<int:id>', methods=['POST'])
def excluir(id):
    excluir_pessoa(id)
    return redirect(url_for('index'))