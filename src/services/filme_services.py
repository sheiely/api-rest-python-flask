from ..models.Filme import Filme
from ..database.config import SessionLocal

db = SessionLocal()

def criar(nome, genero, ano, sinopse, diretor):
    try:
        novoFilme = Filme(nome= nome, genero=genero, ano= ano, sinopse= sinopse, diretor= diretor)
        db.add(novoFilme)
        db.commit()
        return ({
            "message":"Criado com sucesso"
        }, 201)
        
    except Exception as e:
        error = str(e)
        print(error)
        return ({
            "message": "ERRO: ocorreu um erro interno"
        }, 400)
    
def listarPorGenero(genero):
    try:
        filmes = db.query(Filme).filter(Filme.genero==genero).all()
        return  ({
            "message": "busca concluida",
            "filmes": [row.serialize for row in filmes]
        }, 200)
    except Exception as e:
        error = str(e)
        print(error)
        return ({
            "message": "ERRO: "+error
        }, 400)
    

def buscar(id):
    try:
        filme = db.query(Filme).filter(Filme.id==id).first()
        if(filme):
            return  ({
                "message": "busca concluida",
                "filme": filme.serialize
            }, 200)
        raise Exception("Nao foi encontrado nenhum filme")
    except Exception as e:
        error = str(e)
        return ({
            "message": "ERRO: "+error
        }, 400)