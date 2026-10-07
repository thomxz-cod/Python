from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey
from app.database import Base



class Tutor(Base):
    __tablename__ = 'tutores'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    telefone = Column(String(20))
    email = Column(String(100), unique=True)
    


class Animal(Base):
    __tablename__ = 'animais'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome_animal = Column(String(60), nullable=False)
    especie = Column(String(40))
    raca = Column(String(60))
    peso_kg = Column(Float, nullable=False)
    tutor_id = Column(Integer, ForeignKey("tutores.id"))

class Atendimento(Base):
    __tablename__ = 'atendimentos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    data_atend = Column(String(10))
    motivo = Column(String(200), nullable=False)
    valor_cons = Column(Float)
    animal_id = Column(Integer, ForeignKey("animais.id"))