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

def inserir_animal(db: Session, nome_animal: str, especie: str, raca: str, peso_kg: float, tutor_id:int):

    # criar Objeto
    novo = Animal(nome_animal=nome_animal, especie=especie, raca=raca, peso_kg=peso_kg, tutor_id=tutor_id)

    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

def inserir_atendimento(db: Session, data_atend: str, motivo: str, valor_cons: float, animal_id:int):

    # criar Objeto
    novo = Atendimento(data_atend=data_atend, motivo=motivo, valor_cons=valor_cons, animal_id=animal_id)

    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo