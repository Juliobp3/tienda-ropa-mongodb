import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv('MONGO_URI')
DB_NAME = os.getenv('DB_NAME')

try:
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    print('✅ Conectado a MongoDB Atlas')
except Exception as e:
    print(f'❌ Error al conectar a MongoDB: {e}')
    db = None