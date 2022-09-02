from db.database import Database
from pprint import pprint as pp
from bson.objectid import ObjectId

class PessoaDAO:
    def __init__(self):
        self.db = Database(database="s202crud", collection="livros")
        self.collection = self.db.collection
    
    def resetDatabase(self):
        self.db.drop_collection(self.collection)
        self.collection.insert_many(self.dataset)

    def create(self, _id,titulo, autor, ano, preco):
        return self.collection.insert_one({"_id": _id, "titulo": titulo, "autor": autor, "ano": ano, "preco": preco})

    def read(self):
        return self.collection.find()

    def update(self, _id, preco):
        return self.collection.update_one(
            {"_id": _id},
            {
                "$set": {"preco": preco},
                "$currentDate": {"lastModified": True}
            }
        )

    def delete(self, _id):
        return self.collection.delete_one({"_id": _id})

