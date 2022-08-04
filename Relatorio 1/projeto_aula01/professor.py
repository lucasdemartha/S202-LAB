from pessoa import pessoa

class professor (pessoa):
    def __init__(self, nome, especialidade):
        self.nome = nome
        self.especialidade = especialidade

    def toString (self):
        return f'''
        Aula de {self.especialidade}
            Professor: {self.nome}
        '''