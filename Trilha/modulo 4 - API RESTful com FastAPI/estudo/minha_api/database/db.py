from sqlalchemy import create_engine # porta de entrada e o ponto de partida de qualquer aplicação que utiliza o SQLAlchemy

from sqlalchemy.orm import declarative_base, sessionmaker 
# declarative_base -  transforma classes Python comuns em tabelas do banco de dados
# sessionmaker - fábrica de sessões (Sessions) no SQLAlchemy

DATABASE_URL = "sqlite:///./produto.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={'check_same_thread': False} # precisa passar para o SQLite
)

# Fábrica de sessões — cada requisição usa uma sessão própria
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Classe base para os modelos SQLAlchemy
Base = declarative_base()


# Função de dependência — garante que a sessão fecha após cada requisição
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()