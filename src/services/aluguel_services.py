from ..models.Aluguel import Aluguel
from ..models.Filme import Filme
from ..models.Usuario import Usuario
from ..models.Avaliacao import Avaliacao
from ..database.config import SessionLocal
db = SessionLocal()

def criar(filme_id, usuario_id, vencimento_data):
    try:
        filmeExiste = db.query(Filme).filter(Filme.id==filme_id).first()
        usuarioExiste = db.query(Usuario).filter(Usuario.id==usuario_id).first()
        if not filmeExiste:
           raise Exception("Esse filme nao existe")
        if not usuarioExiste:
           raise Exception("Esse Usuario nao existe")
        novoAluguel = Aluguel(filme_id= filme_id, usuario_id=usuario_id, vencimento_data= vencimento_data)
        db.add(novoAluguel)
        db.commit()
        return ({"message":"Alugado com sucesso"}, 201)
        
    except Exception as e:
        error = str(e)
        return ({
            "message": "ERRO: "+error
        }, 400)

def listarPorUsuario(usuario_id):
    try:
        usuarioExiste = db.query(Usuario).filter(Usuario.id==usuario_id).first()
        if not usuarioExiste:
           raise Exception("Esse usuario nao existe")
        alugueis = db.query(Aluguel).filter_by(usuario_id=usuario_id).all()
        alugueisserialized = []
        for aluguel in alugueis:
            avaliacao = db.query(Avaliacao).filter_by(usuario_id=usuario_id, filme_id = aluguel.filme_id).first()
            if(avaliacao):
                alugueisserialized = {**aluguel.serialize, **avaliacao.serialize}
            else:
                alugueisserialized = aluguel.serialize

        return  ({
            "message": "busca concluida",
            "alugueis": alugueisserialized
        }, 200)
    except Exception as e:
        error = str(e)
        return ({
            "message": "ERRO: "+error
        }, 400)


