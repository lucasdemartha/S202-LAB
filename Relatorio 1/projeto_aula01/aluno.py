from pessoa import pessoa

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
