from ..services import usuario_services as srv
from flask import jsonify, make_response, request

def criar():
        entrada = request.get_json()
        msg, codigo = srv.criar(nome = entrada["nome"],
                                celular = entrada["celular"],
                                email = entrada["email"])
        return make_response(msg, codigo)