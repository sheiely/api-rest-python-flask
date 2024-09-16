from ..services import filme_services as srv
from flask import jsonify, make_response, request

def criar():
    entrada = request.get_json()
    
    msg, codigo = srv.criar(nome =entrada["nome"],
                        genero = entrada["genero"],
                        ano = entrada["ano"],
                        sinopse = entrada["sinopse"],
                        diretor = entrada["diretor"])
    return make_response(msg, codigo)

def listarPorGenero(genero):
    msg, codigo = srv.listarPorGenero(genero)
    return make_response(msg, codigo)

def buscar(id):
    msg, codigo = srv.buscar(id =id)
    return make_response(msg, codigo)
        

    
    