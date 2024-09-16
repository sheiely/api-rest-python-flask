from ..services import avaliacao_services as srv
from flask import jsonify, make_response, request


def avaliar():
    try:
        entrada = request.get_json()
        if(entrada["nota"] > 5 or entrada["nota"]<0):
            raise Exception("A nota precisa ser entre 1 a 5")
        msg, codigo = srv.avaliar(filme_id =entrada["filme_id"],
                                usuario_id = entrada["usuario_id"],
                                nota = entrada["nota"])
        return make_response(msg, codigo)
    except Exception as e:
        error = str(e)
        return ({
            "message": "ERRO: "+error
        }, 400)
        
    

