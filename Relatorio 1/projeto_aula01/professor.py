from pessoa import pessoa

class professor (pessoa):
    def __init__(self, nome, especialidade):
        pessoa(nome)
        self.nome = pessoa(nome).nome
        self.especialidade = especialidade

    def toString (self):
        return f'''
        Aula de {self.especialidade}
            Professor: {self.nome}
        '''