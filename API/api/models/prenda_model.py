from api.config.db import db
from bson import ObjectId

class PrendaModel:
    @staticmethod
    def get_all():
        prendas = db.prendas.find()
        return list(prendas)
    
    @staticmethod
    def get_by_id(id):
        return db.prendas.find_one({'_id': ObjectId(id)})
    
    @staticmethod
    def create(data):
        result = db.prendas.insert_one(data)
        return result.inserted_id
    
    @staticmethod
    def update(id, data):
        result = db.prendas.update_one(
            {'_id': ObjectId(id)},
            {'$set': data}
        )
        return result.modified_count
    
    @staticmethod
    def delete(id):
        result = db.prendas.delete_one({'_id': ObjectId(id)})
        return result.deleted_count