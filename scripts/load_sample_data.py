# scripts/load_sample_data.py

import pandas as pd
from pymongo import MongoClient
import os
import sys

# Adiciona o diretório raiz do projeto ao path para importar módulos da app
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.utils.database import DatabaseConnector

# Configurações do MongoDB (usar as mesmas do docker-compose e app.py)
MONGO_URI = "mongodb://eshopuser:eshoppassword@localhost:27017/"
DB_NAME = "eshop_db"

def load_data_from_csv(filepath: str, collection_name: str):
    """
    Carrega dados de um arquivo CSV para uma coleção MongoDB.
    """
    if not os.path.exists(filepath):
        print(f"Erro: Arquivo CSV não encontrado em '{filepath}'")
        return

    try:
        df = pd.read_csv(filepath)
        records = df.to_dict(orient='records')

        db_connector = DatabaseConnector()
        client = db_connector.connect_mongodb(MONGO_URI)
        if client:
            db = client[DB_NAME]
            collection = db[collection_name]
            
            print(f"Inserindo {len(records)} documentos na coleção '{collection_name}'...")
            collection.insert_many(records)
            print(f"Dados do '{filepath}' carregados com sucesso na coleção '{collection_name}'.")
        else:
            print("Não foi possível conectar ao MongoDB.")
    except Exception as e:
        print(f"Erro ao carregar dados do CSV: {e}")

if __name__ == "__main__":
    
    print("Este script é um placeholder. Adapte-o para carregar seus próprios arquivos CSV de exemplo.")
    print("Exemplo: python scripts/load_sample_data.py ../data/sample_customers.csv clientes")
    
    if len(sys.argv) == 3:
        csv_path = sys.argv[1]
        collection = sys.argv[2]
        load_data_from_csv(csv_path, collection)
    else:
        print("Uso: python scripts/load_sample_data.py <caminho_do_csv> <nome_da_colecao>")
