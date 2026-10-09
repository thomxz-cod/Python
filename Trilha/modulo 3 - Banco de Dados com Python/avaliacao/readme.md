# Relatório Final

### 1
autocommit - quando grava no database automaticamente.
o valor False - permite mais gerenciamento na hora de gravar no banco, caso de um erro tem como desfazer antes de gravar direto no database

### 2
db.add() - coloca o objeto na fila pra gravar no db
db.commit() - envia e salva permanente no db
chamar commit() sem add() - não grava nada no db pois não vai ter nada na fila 

### 3
porque é o nome da tabela dentro do banco de dados real, usado pra encontrar o ID.

### 4
colocar um valor maximo é o basico de TI, evita uso de memoria atoa, é um metodo de validar dados etc

### 5
arquivo.db é o banco de dados real usado, se rodar o rodar o main.py ele recriara o arquivo.db, mas voce perdera os dados do arquivo anterior