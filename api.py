from flask import Flask
from flask_restful import Api

from resources.Book import Book
from resources.BookList import BookList

app = Flask(__name__)
api = Api(app)

api.add_resource(BookList, "/books")
api.add_resource(Book, "/books/<int:id>")

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)