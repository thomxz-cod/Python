from app.database import engine, Base, SessionLocal
from app import models #importar para registrar os modelos na BASE
from app.seed import popular_banco
from app.crud import criar_funcionario

# create_all: cria as tabelas que não existem ainda 
# se a tabela ja existe: não apaga, não muda nada 
Base.metadata.create_all(bind=engine)
popular_banco() # popula na mesma hora que cria com o seed

# criar novos usuarios no banco
db = SessionLocal()
try:
    criar_funcionario(db, "Ana Beatriz", "ana@gmail.com", "61999200000", 2000)
finally:
    db.close()