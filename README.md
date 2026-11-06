# api-atletas-fastapi
API REST em Python para cadastro e consulta de atletas, com paginação, busca por nome e CPF e tratamento de CPF duplicado. Feita com FastAPI, SQLAlchemy e fastapi-pagination, com suporte a SQLite e PostgreSQL.
---
Tecnologias

-FastAPI

-SQLAlchemy

-fastapi-pagination

-Uvicorn

-SQLite 

# 1. Clone o repositório e entre na pasta
git clone https://github.com/gabriel-dickson-dev/api-atletas-fastapi
cd SEU_REPOSITORIO

# 2. Crie e ative um ambiente virtual
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Suba a API
uvicorn main:app --reload
