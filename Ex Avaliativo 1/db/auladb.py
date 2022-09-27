from bson import ObjectId
from db.database import Database

class AulaDB:
    def __init__(self):
        self.db = Database(database='atlas-cluster', collection='Aulas')
        self.collection = self.db.collection

    def create(self, aula):
        print(aula)
        ret = self.collection.insert_one({"Aula":aula.assunto,"Professor":aula.professor.toString(),"Alunos":aula.getListaPresenca()})
        return ret.inserted_id

    def read(self, assunto_id : str):
        return self.collection.find({'Aula': assunto_id})

    def update(self,assunto_id : str, assunto_modificado : str):
        return self.collection.update_one(
            {"Aula": assunto_id},
            {
                "$set": {"Aula": assunto_modificado},
                "$currentDate": {"lastModified": True}
            }
        )

    def delete(self, assunto_id : str):
        return self.collection.delete_one({"Aula": assunto_id})