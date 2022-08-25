from db.database import Database
from helper.WriteAJson import writeAJson
from dataset.pessoa_dataset import dataset as pessoa_dataset
from dataset.carro_dataset import dataset as carro_dataset
from dataset.produto_database import dataset as produto_database

pessoas = Database(
    database="database",
    collection="pessoas",
    dataset=pessoa_dataset
)
pessoas.resetDatabase()

compras = Database(
    database="database",
    collection="produtos",
    dataset= produto_database
    )
compras.resetDatabase()

carros = Database(
    database="database",
    collection="carros",
    dataset=carro_dataset
)
carros.resetDatabase()

result1 = compras.collection.aggregate([
    {"$lookup":
        {
            "from": "pessoas",
            "localField": "cliente_id",
            "foreignField": "_id",
            "as": "dono"
        }
    },
        {"$group": {"_id": "$dono.nome", "total": {"$sum": "$total"} } }, # formata os documentos
        {"$sort": {"total": -1} }, # ordena os documentos
        {"$unwind": '$_id'}, 
        {"$project": {
            "nome": 1,
            "total": 1,
            "desconto": {
                "$cond": {"if": {"$gte": ["$total", 10]}, "then": "true", "else": "false"}
            }
        }}
])

writeAJson(result1, "result1")

