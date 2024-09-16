from flask import request, make_response
from ..models.Usuario import Usuario
from ..database.config import SessionLocal

db = SessionLocal()


def criar(nome, celular, email):
    try:
        usuarioEmailIgual = db.query(Usuario).filter(Usuario.email==email).first()
        if(usuarioEmailIgual):
            raise Exception("Ja existe um usuario com esse email")
        novoUsuario = Usuario(nome= nome, celular=celular, email= email)
        db.add(novoUsuario)
        db.commit()
        return ({
            "message":"Criado com sucesso"
        }, 201)
        
    except Exception as e:
        error = str(e)
        return ({
            "message": "ERRO: "+error
        }, 400)
    
