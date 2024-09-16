from sqlalchemy import Column, Integer, ForeignKey
from ..database.config import Base

class Avaliacao(Base):
    __tablename__ = "Avaliacoes"

    id = Column(Integer, primary_key=True, nullable=False)
    filme_id = Column(Integer, ForeignKey("Filmes.id"), nullable=False)
    usuario_id = Column(Integer, ForeignKey("Usuarios.id"), nullable=False)
    nota= Column(Integer, nullable=False)
    @property
    def serialize(self):
        return {
            "id": self.id,
            "filme_id": self.filme_id,
            "usuario_id": self.usuario_id,
            "nota": self.nota,
        }