from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from ..database.config import Base



class Aluguel(Base):
    __tablename__ = "Alugueis"
     
    id = Column(Integer, primary_key=True, nullable=False)
    filme_id = Column(Integer, ForeignKey("Filmes.id"), nullable=False)
    usuario_id = Column(Integer, ForeignKey("Usuarios.id"), nullable=False)
    criacao_data = Column(DateTime, server_default=func.now(), nullable=False)
    vencimento_data= Column(DateTime, nullable=False)
    filme = relationship('Filme', backref='Alugueis')
    @property
    def serialize(self):
        return {
            "id": self.id,
            "filme": self.filme.serialize,
            "usuario_id": self.usuario_id,
            "criacao_data": self.criacao_data,
            "vencimento_data": self.vencimento_data,
        }
