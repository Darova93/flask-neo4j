from flask_restful import Resource, Api, reqparse, abort, marshal, fields
from data.books import books, bookFields

from neo4j import GraphDatabase

class Book(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument("title", type=str, location="json")
        self.reqparse.add_argument("author", type=str, location="json")
        self.reqparse.add_argument("length", type=int, location="json")
        self.reqparse.add_argument("rating", type=float, location="json")

        super(Book, self).__init__()

    def get(self, id):
        book = [book for book in books if book['id'] == id]

        if(len(book) == 0):
            abort(404)

        return{"book": marshal(book[0], bookFields)}
    
    def put(self,id):
        book = [book for book in books if book['id'] == id]

        if(len(book)) == 0:
            abort(404)
        
        book = book[0]

        args = self.reqparse.parse_args()
        for k, v in args.items():
            if v is not None:
                book[k] = v

        return{"book": marshal(book, bookFields)}

    def delete(self, id):
        book = [book for book in books if book['id'] == id]

        if(len(book) == 0):
            abort(404)

        books.remove(book[0])

        return 201
        