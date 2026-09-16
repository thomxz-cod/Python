-- Comentario
create database escola;

use escola;

create table alunos (
	id_aluno int auto_increment primary key,
    nome varchar(150) not null,
    cpf varchar(14) unique not null,
    email varchar(100) not null unique,
    data_nascimento date,
    telefone varchar(20),
    ativo tinyint(1) default 1
);

insert into alunos (nome, cpf, email, data_nascimento, telefone)
values
("toin","999.111.000-67","toin@gmail.com","2008-06-25","(+55) 61 9 99172008"),
("debis","111.555.222-86","debis@gmail.com","2008-12-07","(+55) 61 9 99999999"),
("bebezin","141.355.626-96","baby@gmail.com","2008-12-07","(+55) 61 9 88888888");

select * from alunos; -- consulta tudo
select nome, email from alunos; -- consulta apenas nome e email
select * from alunos where nome like "t%"; -- consulta apenas onde o nome começa com t
