# from pprintpp import pprint as pp
from db.database import Graph
from helper.write_a_json import write_a_json as wj

db = Graph(uri='bolt://44.210.129.174:7687', user='neo4j', password='usage-accusation-chairmen')

# Questão 01
# A RENZO
wj(db.execute_query("MATCH(r:Teacher{name:'Renzo'}) RETURN r.ano_nasc, r.cpf;"),'1A')

# B STARTS WITH
wj(db.execute_query("MATCH(r:Teacher) WHERE r.name STARTS WITH 'M' RETURN r.name, r.cpf;"),'1B')

# C ALL CITY
wj(db.execute_query("MATCH(r:City) RETURN r.name"),'1C')

# D CONDITION
wj(db.execute_query("MATCH(r:School) WHERE r.number >= 150 AND r.number <= 550 RETURN r.name, r.address"),'1D')

# Questão 02
# A MINMAX
wj(db.execute_query("MATCH(r:Teacher) return MIN(r.ano_nasc), MAX(r.ano_nasc)"),'2A')

# B AVG
wj(db.execute_query("MATCH(r:City) return AVG(r.population)"),'2B')

# C REPLACE
wj(db.execute_query("MATCH(r:City) WHERE r.cep = '37540-000' RETURN REPLACE(r.name, 'a', 'A')"),'2C')

# D SUBSTRING
wj(db.execute_query("MATCH(r:Teacher) RETURN SUBSTRING(r.name, 3, 1)"),'2D')

# Questão 03
# A CLASS
class TeacherCrud(object):

    def __init__(self):
        self.db = db

    def create(self, teacher):
        return self.db.execute_query('create (r:Teacher{name: $name, ano_nasc: $ano_nasc, cpf: $cpf}) RETURN r',
                                     {'name': teacher['name'], 'ano_nasc': teacher['ano_nasc'], 'cpf': teacher['cpf']})

    def read(self, aux):
        return self.db.execute_query('match (r:Teacher{name: $name}) RETURN r',
                                     {'name': aux['name']})

    def delete(self, aux):
        return self.db.execute_query('match (r:Teacher{name: $name}) DELETE r',
                                     {'name': aux['name']})

    def update(self, aux, cpf):
        return self.db.execute_query('match (r:Teacher{name: $name}) SET r.cpf = $cpf RETURN r',
                                     {'name': aux, 'cpf': cpf})

# B CREATE
tc = TeacherCrud()

auxCREATE = {
    'name': 'Chris Lima',
    'ano_nasc': 1956,
    'cpf': '189.052.396-66'
}

wj(tc.create(auxCREATE), '3B')

# C READ
auxREAD = {
    'name': 'Chris Lima',
}
wj(tc.read(auxREAD), '3C')

# D UPDATE
auxUPDATE = 'Chris Lima'
auxCPF = '162.052.777-77'
wj(tc.update(auxUPDATE, auxCPF), '3D')

