from db.auladb import AulaDB
from db.database import Database
from helper.WriteAJson import writeAJson
from classes import *


if __name__ == '__main__':

    aula = AulaDB()

    op = 0

    while op != 5:
        op = int(input(f'Menu S202:\n1 - Criar aula\n2 - Modificar aula \n3 - Deletar aula\n'
              f'4 - Listar todas aulas\n5 - Sair\nOpção:'))

        if op == 1:

            assunto = input('Assunto da aula:')
            prof = input('Nome do professor: ')
            especialidade = input('Especialidade do professor: ')
            professor = Professor(prof,especialidade)
            
            alunos = []
            qntAlunos = int(input('Quantos alunos quer cadastrar? '))
            for qntAlunos in range(0, qntAlunos):
                nome = input('Nome do aluno: ')
                matricula = input('Matricula do aluno: ')
                curso = input('Curso do aluno: ')
                periodo = input('Periodo do aluno: ')
                alunos.append(Aluno(nome, matricula, curso, periodo))

            aula1 = Aula(assunto, alunos, professor)
            aula.create(aula1)

        if op == 2:
            assunto_id = input('Digite o assunto da aula que irá modificar:')
            assunto_modificado = input('Digite um novo assunto para a aula:')
            assunto = aula.update(assunto_id, assunto_modificado)               

        if op == 3:
            assunto = input('Digite o assunto da aula que irá deletar:')
            aula.delete(assunto)

        if op == 4:
            assunto = input('Digite o assunto da aula que deseja:')
            ret = aula.read(assunto)
            writeAJson(ret, 'aula')

        if op == 5:
            break