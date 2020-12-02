from flask_restful import Resource, Api, reqparse, abort, marshal, fields
from data.books import books, bookFields

from neo4j import GraphDatabase

class BookList(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            "title", 
            type=str, 
            required=True, 
            help="The title of the book must be provided", 
            location="json"
        )
        self.reqparse.add_argument(
            "author",
            type=str,
            required=True,
            help="The author of the book must be provided",
            location="json"
        )
        self.reqparse.add_argument(
            "length",
            type=int,
            required=True,
            help="The length of the book (in pages)",
            location="json"
        )
        self.reqparse.add_argument(
            "rating",
            type=float,
            required=True,
            help="The rating must be provided",
            location="json"
        )
        self.driver = GraphDatabase.driver('localhost', auth=('neo4j', 'admin'))

    def get(self):
        with self.driver.session() as session:
            session.write_transaction(self._create_and_return_greeting, 'Hello world')
        # return{"books": [marshal(book, bookFields) for book in books]}

    def _create_and_return_greeting(self, tx, message):
        result = tx.run("CREATE (a:Greeting) "
                        "SET a.message = $message "
                        "RETURN a.message + ', from node ' + id(a)", message=message)
        return result.single()[0]
        
    def post(self):
        args = self.reqparse.parse_args()
        book = {
            "id": books[-1]['id'] + 1 if len(books) > 0 else 1,
            "title": args["title"],
            "author": args["author"],
            "length": args["length"],
            "rating": args["rating"],
        }

        books.append(book)
        return{"book": marshal(book, bookFields)}, 201