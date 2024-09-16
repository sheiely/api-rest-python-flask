# FilmesTop

FilmesTop é uma aplicação web desenvolvida com Flask para gerenciar filmes e seus respectivos aluguéis.

## Funcionalidades

- Cadastro de usuários
- Listagem de filmes
- Registro de aluguéis

## Tecnologias Utilizadas

- **Flask**: Framework web
- **PostgreSQL**: Banco de dados relacional
- **SQLAlchemy**: ORM para banco de dados

## Instalação

1. Tenha na sua máquina instalado o Python 3.10+ 

2. Clone o repositório

```bash
git clone https://github.com/sheieley/filmes-top.git
cd filmes-top
```

3. Crie o ambiente virtual e ative
````bash
python3 -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
````

4. Instale as dependencias do projeto
````bash
pip install -r requirements.txt
````

5. Caso opte por iniciar o PostgreSql pelo Docker ao invés do PGAdmin, você pode:
````
docker run --name postgres_filmes_top -e POSTGRES_USER=seu_usuario -e POSTGRES_PASSWORD=sua_senha -e POSTGRES_DB=filmes_top_db -p 5432:5432 -d postgres
````

6. Execute o projeto
````
flask run
````

Para verificar a documentação da aplicação, verifique a rota "\swagger"
