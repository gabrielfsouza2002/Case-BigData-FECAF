import pymongo
import redis
import pandas as pd
from typing import Optional
import os

class DatabaseConnector:
    def __init__(self):
        self.mongo_client = None
        self.redis_client = None
        
    def connect_mongodb(self, uri: str = "mongodb://localhost:27017/"):
        """Conecta ao MongoDB"""
        try:
            self.mongo_client = pymongo.MongoClient(uri)
            # Testa a conexão
            self.mongo_client.admin.command('ping')
            return self.mongo_client
        except Exception as e:
            print(f"Erro ao conectar ao MongoDB: {e}")
            return None
    
    def connect_redis(self, host: str = "localhost", port: int = 6379):
        """Conecta ao Redis"""
        try:
            self.redis_client = redis.Redis(
                host=host, 
                port=port, 
                decode_responses=True
            )
            # Testa a conexão
            self.redis_client.ping()
            return self.redis_client
        except Exception as e:
            print(f"Erro ao conectar ao Redis: {e}")
            return None
    
    def get_mongodb_data(self, database: str, collection: str, 
                        query: dict = {}, limit: Optional[int] = None):
        """Recupera dados do MongoDB"""
        if not self.mongo_client:
            return pd.DataFrame()
        
        db = self.mongo_client[database]
        col = db[collection]
        
        cursor = col.find(query)
        if limit:
            cursor = cursor.limit(limit)
            
        return pd.DataFrame(list(cursor))