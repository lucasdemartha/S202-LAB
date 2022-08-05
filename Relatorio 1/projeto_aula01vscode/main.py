class pessoa():
    def __init__(self, nome):
        self.nome = nome

class aluno(pessoa):
    def __init__(self,nome ,matricula, curso, periodo):
        pessoa(nome)
        self.nome = pessoa(nome).nome
        self.matricula = matricula
        self.curso = curso
        self.periodo = periodo

    def toString(self):
        return f'''
                nome: {self.nome}
                matricula: {self.matricula}
                curso: {self.curso}
                periodo: {self.periodo}
        '''

class professor (pessoa):
    def __init__(self, nome, especialidade):
        pessoa(nome)
        self.nome = pessoa(nome).nome
        self.especialidade = especialidade

    def toString (self):
        return f'''
            Professor: {self.nome}
            Especialidade: {self.especialidade}
        '''

class aula ():
    def __init__(self,assunto):
        self.assunto = assunto
        self.aluno = ''
        self.professor = ''


    def getListaPresenca(self):
        print(f'Aula de {self.assunto}')
        teste = self.professor.toString()
        print(f'{teste}')
        listaPresenca = "\tAlunos Presentes \n"
        for presenca in self.aluno:
            listaPresenca += presenca.toString()

        return listaPresenca

if __name__ == '__main__':
    aula1 = aula(assunto = "MongoDB")


    lista1 = [aluno(nome = "Bruno", matricula = 14, curso = "GES", periodo = 7),
              aluno(nome = "Leonardo", matricula = 44, curso = "GEC", periodo = 6),
              aluno(nome = "Davi", matricula = 54, curso = "GES", periodo = 2)]

    professor1 = professor(nome = "Renzo", especialidade = "Software")

    aula1.aluno = lista1
    aula1.professor = professor1

    print(professor1.toString())
    print(aula1.getListaPresenca())