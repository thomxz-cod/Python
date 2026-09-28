from app.database import engine, Base, SessionLocal
from app import models #importar para registrar os modelos na BASE
from app.seed import popular_banco
from app.crud_funcionario import *
from app.crud_departamento import *

# create_all: cria as tabelas que não existem ainda 
# se a tabela ja existe: não apaga, não muda nada 
Base.metadata.create_all(bind=engine)
popular_banco() # popula na mesma hora que cria com o seed

# criar novos funcionarios no banco
db = SessionLocal()
try: # funcionarios
    criar_funcionario(db, "Ana Beatriz", "ana@gmail.com", "61999200000", 2000)
    
    funcionario = buscar_funcionario(db, 5)
    if funcionario:
        print(f'\nFuncionario: {funcionario.nome}')

    atualizado = atualizar_funcionario(db, 5, telefone=10102008)
    print(f'{atualizado.nome}: telefone: {atualizado.telefone}')

    desativar_funcionario(db, 4)
    funcionarios = listar_funcionarios(db)
    print(f'Total: {len(funcionarios)} funcionarios!')
    for funcionario in funcionarios:
        print(f'{funcionario.nome} - R${funcionario.salario}')

finally:
    db.close()


try: # departamentos
    criar_departamento(db, "Departamento Louco", "DL")

    atualizar_departamento(db, 5, sigla="DP_L")

    departamentos = listar_departamentos(db)
    print(f'Total: {len(funcionarios)} departamentos!')
    for departamento in departamentos:
        print(f'{departamento.sigla} - {departamento.ativo}')

    desativar_departamento(db, 3)
    
finally:
    db.close()