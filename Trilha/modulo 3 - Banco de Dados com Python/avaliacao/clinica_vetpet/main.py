from app.database import engine, Base
from app import models

# Criar todas as tabelas que não existem no banco de dados
Base.metadata.create_all(bind=engine)
