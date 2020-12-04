from flask_restful import fields

errorFields = {
    "code": fields.Integer,
    "message": fields.String,
    "type": fields.String,
}