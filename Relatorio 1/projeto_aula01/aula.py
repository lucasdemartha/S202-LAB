
class aula ():
    def __init__(self, assunto):
        self.assunto = assunto


    def getListaPresenca(self):
        listaPresenca = "\t\t\tAlunos Presentes \n"
        for presenca in self.assunto:
            listaPresenca += presenca.toString()

        return listaPresenca