from api.config.db import db
from bson import ObjectId

class UsuarioModel:
    @staticmethod
    def get_all():
        usuarios = db.usuarios.find()
        return list(usuarios)
    
    @staticmethod
    def get_by_id(id):
        return db.usuarios.find_one({'_id': ObjectId(id)})
    
    @staticmethod
    def create(data):
        result = db.usuarios.insert_one(data)
        return result.inserted_id
    
    @staticmethod
    def update(id, data):
        result = db.usuarios.update_one(
            {'_id': ObjectId(id)},
            {'$set': data}
        )
        return result.modified_count
    
    @staticmethod
    def delete(id):
        result = db.usuarios.delete_one({'_id': ObjectId(id)})
        return result.deleted_count