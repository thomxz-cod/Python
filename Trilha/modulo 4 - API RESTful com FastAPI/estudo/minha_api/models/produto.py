from sqlalchemy import Column, Integer, String, Float, Boolean
from database.db import Base

class Produto(Base):
    __tablename__ = "produtos"

    id          = Column(Integer, primary_key=True, index=True)
    nome        = Column(String(100), nullable=False)
    descricao   = Column(String(500), nullable=True)
    preco       = Column(Float, nullable=False)
    estoque     = Column(Integer, default=0)
    ativo       = Column(Boolean, default=True)

""" 
    ORM (Object-Relational Mapper) permite trabalhar com o banco de dados usando classes Python, sem escrever SQL diretamente.
    Produto(nome='Mouse', preco=89.90) → INSERT INTO produtos (nome, preco) VALUES ('Mouse', 89.90)
    db.query(Produto).all() → SELECT * FROM produtos
"""