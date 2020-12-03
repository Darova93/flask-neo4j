from flask_restful import Resource, Api, reqparse, abort, marshal, fields
from neo4j import GraphDatabase

class Neo4J(Resource):
    def __init__(self):
        self.driver = GraphDatabase.driver('localhost', auth=('neo4j', 'admin'))

    def get(self):
        with self.driver.session() as session:
            session.write_transaction(self._create_and_return_greeting, 'Hello world')
    
    def _create_and_return_greeting(self, tx, message):
        result = tx.run("CREATE (a:Greeting) "
                        "SET a.message = $message "
                        "RETURN a.message + ', from node ' + id(a)", message=message)
        return result.single()[0]