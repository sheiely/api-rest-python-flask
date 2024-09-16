from sqlalchemy import Column, Integer, String
from ..database.config import Base


class Usuario(Base):
    __tablename__ = "Usuarios"

    id = Column(Integer, primary_key=True, nullable=False)
    nome = Column(String(100), nullable=False)
    celular = Column(String(20), nullable=False)
    email= Column(String(50), nullable=False, unique=True)

    def __repr__(self):
        return f"<User {self.nome} {self.id}"