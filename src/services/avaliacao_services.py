from flask import request, make_response
from ..models.Avaliacao import Avaliacao
from ..models.Aluguel import Aluguel
from ..models.Filme import Filme
from ..database.config import SessionLocal
db = SessionLocal()

def avaliar(filme_id, usuario_id, nota):
    try:
        alugueisUsuario = db.query(Aluguel).filter(Aluguel.usuario_id == usuario_id, Aluguel.filme_id == filme_id).first()
        if(alugueisUsuario):
            if(db.query(Avaliacao).filter(Avaliacao.usuario_id==usuario_id, Avaliacao.filme_id == filme_id).first()):
                raise Exception("Usuario ja avaliou esse filme") 
                
            novaAvaliacao = Avaliacao(filme_id= filme_id, usuario_id=usuario_id, nota= nota)
            
            filme = db.query(Filme).filter(Filme.id==filme_id).first()
            db.add(novaAvaliacao)
            db.commit()
            
            avFilme = db.query(Avaliacao).filter(Avaliacao.filme_id == filme_id).all()
            somatorioNotas = 0
            totalAv = len(avFilme)
            for avaliacoes in avFilme:
                somatorioNotas += avaliacoes.nota
            filme.nota_final = somatorioNotas/totalAv
            filme.total_avaliacoes = totalAv
            db.commit()




            return ({
                "message":"Avaliado com sucesso"
            }, 201)
        raise Exception("Erro ao procurar aluguel - usuario e/ou filme nao existem, ou usuario nao alugou esse filme")   
    except Exception as e:
        error = str(e)
        db.rollback()
        return ({
            "message": "ERRO: "+error
        }, 400)
    

