from aluno import aluno
from professor import professor
from aula import aula
from pessoa import pessoa

aula1 = aula(assunto = "MongoDB")

pessoa1 = pessoa(nome = "Bruno")
pessoa2 = pessoa(nome = "Leonardo")
pessoa3 = pessoa(nome = "Davi")

aluno1 = aluno(pessoa1.nome, matricula = 14, curso = "GES", periodo = 7)
aluno2 = aluno(pessoa2.nome,matricula = 44, curso = "GEC", periodo = 6)
aluno3 = aluno(pessoa3.nome,matricula = 54, curso = "GES", periodo = 2)

professor1 = professor(nome = "Renzo", especialidade = "MongoDB")

turma = [aluno1, aluno2, aluno3]

aul = aula(assunto=turma)
print(professor1.toString())
print(aul.getListaPresenca())