from sqlalchemy import Column, Integer, String

from database import Base


class Atleta(Base):
    __tablename__ = "atletas"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(255), nullable=False)
    cpf = Column(String(11), unique=True, nullable=False)
    centro_treinamento = Column(String(255))
    categoria = Column(String(255))

    # Relacionamento com tabela de treinos (opcional)
    # treinos = relationship("Treino", backref="atleta")
