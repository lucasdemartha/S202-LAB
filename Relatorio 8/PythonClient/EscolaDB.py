from helper.write_a_json import write_a_json
from db.database import Graph

class EscolaDB(object):
    def __init__(self):
        self.db = Graph(uri='bolt://44.210.130.116:7687',
                        user='neo4j', password='cranks-linkages-painter')

    def create(self, person):
        return self.db.execute_query('CREATE (n:Person {name:$name, age:$age, area:$area}) return n',
                                     {'name': person['name'], 'age': person['age'], 'area': person['area']})

    def create_matter(self, matter):
        return self.db.execute_query('CREATE (n:Matter {subject:$subject, time:$time}) return n',
                                     {'subject': matter['subject'], 'time': matter['time']})

    def read_by_name(self, person):
        return self.db.execute_query('MATCH (n:Person {name:$name}) RETURN n',
                                     {'name': person['name']})
    
    def read_all_nodes(self):
        return self.db.execute_query('MATCH (n) RETURN n')

    def update_age(self, person):
        return self.db.execute_query('MATCH (n:Person {name:$name}) SET n.age = $age RETURN n',
                                     {'name': person['name'], 'age': person['age']})

    def delete(self, person):
        return self.db.execute_query('MATCH (n:Person {name:$name}) DELETE n',
                                     {'name': person['name']})

    def delete_all_nodes(self):
        return self.db.execute_query('MATCH (n) DETACH DELETE n')

    def create_relation(self, person, matter, year):
        return self.db.execute_query(
            'MATCH (n:Person {name:$name}), (m:Matter {subject:$subject}) CREATE (n)-[r:TEACHES{year: $year}]->(m) RETURN n, r, m',
            {'name': person['name'], 'subject': matter['subject'], 'year': year})

    def read_relation(self, person, matter):
        return self.db.execute_query('MATCH (n:Person {name:$name})-[r]->(m:Matter {subject:$subject}) RETURN n, r, m',
                                     {'name': person['name'], 'subject': matter['subject']})