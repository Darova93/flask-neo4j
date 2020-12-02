from flask_restful import fields

books = [
    {
        "id": 1,
        "title": "Zero to One",
        "author": "Peter Thiel",
        "length": 195,
        "rating": 4.17,
    },
    {
        "id": 2,
        "title": "Atomic Habits",
        "author": "James Clear",
        "length": 319,
        "rating": 4.35,
    }
]

bookFields = {
    "id": fields.Integer,
    "title": fields.String,
    "author": fields.String,
    "length": fields.Integer,
    "rating": fields.Float,
}