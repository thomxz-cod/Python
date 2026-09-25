from aula.app.database import engine, Base
from aula.app import models #importar para registrar os modelos na BASE
from aula.app.seed import popular_banco

# create_all: cria as tabelas que não existem ainda 
# se a tabela ja existe: não apaga, não muda nada 
Base.metadata.create_all(bind=engine)
popular_banco()
print('Pronto')