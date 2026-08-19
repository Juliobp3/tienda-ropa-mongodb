from api.config.db import db
from bson import ObjectId

class VentaModel:
    @staticmethod
    def get_all():
        ventas = db.ventas.find()
        return list(ventas)
    
    @staticmethod
    def get_by_id(id):
        return db.ventas.find_one({'_id': ObjectId(id)})
    
    @staticmethod
    def create(data):
        result = db.ventas.insert_one(data)
        return result.inserted_id
    
    @staticmethod
    def update(id, data):
        result = db.ventas.update_one(
            {'_id': ObjectId(id)},
            {'$set': data}
        )
        return result.modified_count
    
    @staticmethod
    def delete(id):
        result = db.ventas.delete_one({'_id': ObjectId(id)})
        return result.deleted_count