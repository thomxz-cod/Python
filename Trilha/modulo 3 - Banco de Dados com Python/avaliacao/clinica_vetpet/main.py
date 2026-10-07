from app.database import engine, Base, SessionLocal
from app import models
from app.crud import *

# Criar todas as tabelas que não existem no banco de dados
Base.metadata.create_all(bind=engine)

db = SessionLocal()
try:
    inserir_tutor(db, "Toin", "toin@gmail.com", "61999200000")
    
finally:
    db.close()

db = SessionLocal()
try:
    inserir_animal(db, "Nina", "caramelo", "cachorro", 12, 1)
finally:
    db.close()
