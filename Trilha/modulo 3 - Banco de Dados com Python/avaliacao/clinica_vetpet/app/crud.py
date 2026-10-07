from sqlalchemy.orm import Session
from app.models import Atendimento, Tutor, Animal

def inserir_tutor(db: Session, nome_completo: str, telefone: str, email: str):
    # verficar se o email ja existe
    existe = db.query(Tutor).filter(
        Tutor.email == email
    ).first()

    if existe:
        print(f'E-mail {email} já cadastrado!!')
        return None

    # criar Objeto
    novo = Tutor(nome=nome_completo, email=email, telefone=telefone)

    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo