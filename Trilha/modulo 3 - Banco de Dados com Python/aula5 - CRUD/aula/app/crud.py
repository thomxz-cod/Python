from sqlalchemy.orm import Session
from app.models import Funcionario

def criar_funcionario(db: Session, nome: str, email: str, telefone: str, salario :float):
    # verficar se o email ja existe
    existe = db.query(Funcionario).filter(
        Funcionario.email == email
    ).first()

    if existe:
        print(f'E-mail {email} já cadastrado!!')
        return None

    # criar Objeto
    novo = Funcionario(nome=nome, email=email, telefone=telefone, salario=salario)

    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo
