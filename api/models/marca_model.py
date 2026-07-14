from api.config.db import db
from bson import ObjectId

class MarcaModel:
    @staticmethod
    def get_all():
        marcas = db.marcas.find()
        return list(marcas)
    
    @staticmethod
    def get_by_id(id):
        return db.marcas.find_one({'_id': ObjectId(id)})
    
    @staticmethod
    def create(data):
        result = db.marcas.insert_one(data)
        return result.inserted_id
    
    @staticmethod
    def update(id, data):
        result = db.marcas.update_one(
            {'_id': ObjectId(id)},
            {'$set': data}
        )
        return result.modified_count
    
    @staticmethod
    def delete(id):
        result = db.marcas.delete_one({'_id': ObjectId(id)})
        return result.deleted_count
    
    @staticmethod
    def get_by_nombre(nombre):
        return db.marcas.find_one({'nombre': nombre})