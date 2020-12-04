from flask_restful import fields

imageFields = {
    "filename": fields.String,
    "size": fields.String,
    "type": fields.String,
    "path": fields.String,
    "publicUrl": fields.String,
}