from helper.WriteAJson import writeAJson

class Pessoa(object):
    def __init__(self, nome):
        self.nome = nome

class Professor(Pessoa):
    def __init__(self, especialidade, nome):
        Pessoa.__init__(self, nome)
        self.especialidade = especialidade

    def toString(self):
        return {"Nome": self.nome, "Especialidade": self.especialidade}


class Aluno(Pessoa):
    def __init__(self, nome: str ,matricula: int, curso: str, periodo: int):
        super().__init__(nome)
        self.matricula = matricula
        self.curso = curso
        self.periodo = periodo


    def toString(self):
        return [{'Nome': self.nome, 'Matricula': self.matricula, 'Curso': self.curso, 'Periodo': self.periodo}]


class Aula(object):
    def __init__(self,assunto,lista_presenca,professor):
        self.assunto = assunto
        self.lista_presenca = lista_presenca
        self.professor = professor


    def getListaPresenca(self) -> str:
        list = f'''
        Aula de {self.assunto}
        Professor: {self.professor.toString()}
        '''
        for aluno in self.lista_presenca:
            list += str(aluno.toString()) + ","
        writeAJson(list, "lista")
        return list