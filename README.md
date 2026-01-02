:

🐍 Sistema de Cadastro de Registros com Flask + MySQL

- Aplicação web desenvolvida em Python com o microframework Flask, utilizando a arquitetura MVC e o mecanismo de templates Jinja2.
Permite a listagem de registros com paginação, exibindo 5 registros por página. O projeto utiliza MySQL como banco de dados, rodando em um container Docker.

🚀 Funcionalidades

- Listagem de registros paginada (5 por página)

- Botões para navegação entre páginas

- Renderização dinâmica com Jinja2

- Estrutura limpa com padrão MVC

- Integração com banco de dados relacional via MySQL Connector

🛠 Tecnologias Utilizadas
- Python 3.10+

- Flask

- Jinja2

- MySQL

- Docker

- HTML + Bootstrap

🗂 Estrutura MVC
models/: Representações dos dados (conexão com o MySQL)

controllers/: Regras de negócio e controle de fluxo

templates/: Views HTML com Jinja2

app.py: Arquivo principal da aplicação

💻 Como Executar Localmente
Pré-requisitos
- Python 3 instalado

- Docker e Docker Compose

- Pip ou pipenv

Passo a passo
Clone o repositório:

git clone https://github.com/seuusuario/nome-do-repo.git
cd nome-do-repo

Suba o banco de dados MySQL com Docker:
docker-compose up -d

Instale as dependências:
pip install -r requirements.txt

Rode a aplicação:
python app.py

Acesse no navegador:
http://localhost:5000

🔌 Banco de Dados

O container do MySQL roda com as seguintes configurações (definidas em docker-compose.yml):

environment:
  - MYSQL_ROOT_PASSWORD=123456
  - MYSQL_DATABASE=flask_app


👨‍💻 Autor
Desenvolvido por Alexandre de Souza Eustaquio.

Feedbacks e contribuições são sempre bem-vindos!




![image](https://github.com/user-attachments/assets/91fc86c3-e330-4a3c-8bbd-a27c88008062)
