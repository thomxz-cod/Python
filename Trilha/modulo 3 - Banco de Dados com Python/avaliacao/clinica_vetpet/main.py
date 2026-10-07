from app.database import engine, Base, SessionLocal
from app import models
from app.crud import *

# Criar todas as tabelas que não existem no banco de dados
Base.metadata.create_all(bind=engine)

db = SessionLocal()
try:
    inserir_tutor(db, "Toin", "toin@gmail.com", "61999200000")
    inserir_tutor(db, "Dinha", "dinha@gmail.com", "61999200067")

    inserir_animal(db, "Nina", "caramelo", "cachorro", 12, 1)
    inserir_animal(db, "Nico", "gato preto", "gato", 4, 1)
    inserir_animal(db, "Floquinho", "shih tzu", "cachorro", 10, 2)

    inserir_atendimento(db, "14/11/2026", "velhice", 200, 1)
    inserir_atendimento(db, "08/10/2026", "bixeira", 140, 2)
    inserir_atendimento(db, "10/10/2026", "tosar", 100, 3)


    print(f"""
Tutores inseridos:
Nome: Toin - ID: 1
Nome: Dinha - ID: 2

Animais inseridos:
Nome: Nina - raça: caramelo
Nome: Nico - raça: gato preto
Nome: Floquinho - raça: shih tzu

Atendimentos inseridos:
Atendimento: velhice - R$: 200
Atendimento: bixeira - R$: 140
Atendimento: tosar - R$: 100

""")
    

finally:
    db.close()
