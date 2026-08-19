from api.config.db import db
from bson import ObjectId
import bcrypt

class UsuarioModel:
    @staticmethod
    def get_all():
        usuarios = db.usuarios.find()
        return list(usuarios)
    
    @staticmethod
    def get_by_id(id):
        return db.usuarios.find_one({'_id': ObjectId(id)})
    
    @staticmethod
    def get_by_email(email):
        """Buscar usuario por email"""
        return db.usuarios.find_one({'email': email})
    
    @staticmethod
    def create(data):
        """Crear un nuevo usuario con contraseña encriptada"""
        password = data.get('password')
        if password:
            hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            data['password'] = hashed.decode('utf-8')
        
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
    
    @staticmethod
    def verify_password(usuario, password):
        """Verificar si la contraseña es correcta"""
        if usuario and 'password' in usuario:
            return bcrypt.checkpw(password.encode('utf-8'), usuario['password'].encode('utf-8'))
        return False