from ..services import aluguel_services as srv
from flask import jsonify, make_response, request

def criar():
    entrada = request.get_json()
    msg, codigo = srv.criar(filme_id = entrada["filme_id"],
                            usuario_id = entrada["usuario_id"],
                            vencimento_data = entrada["vencimento_data"])
    return make_response(msg, codigo)

def listarPorUsuario(usuario_id):
    msg, codigo = srv.listarPorUsuario(usuario_id = usuario_id)
    return make_response(msg, codigo)

