from sqlalchemy import Column, Integer, String, Text, Float
from ..database.config import Base


class Filme(Base):
    __tablename__ = "Filmes"

    id = Column(Integer, primary_key=True, nullable=False)
    nome =Column(String(100), nullable=False)
    genero = Column(String(100), nullable=False)
    ano = Column(Integer, nullable=False)
    sinopse =  Column(Text(), nullable=False)
    diretor = Column(String(100), nullable=False)
    total_avaliacoes =  Column(Integer, default=0)
    nota_final = Column(Float, default=0)
    
    @property
    def serialize(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "genero": self.genero,
            "ano": self.ano,
            "sinopse": self.sinopse,
            "diretor": self.diretor,
            "total_avaliacoes": self.total_avaliacoes,
            "nota_final": self.nota_final
        }