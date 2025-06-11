#!/usr/bin/env python3
"""
Script para inicializar os bancos de dados com dados de exemplo
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.utils.data_generator import generate_customers, generate_products, generate_orders
from app.utils.database import DatabaseConnector
import json

def main():
    # Conecta aos bancos
    db = DatabaseConnector()
    
    # MongoDB
    mongo = db.connect_mongodb()
    if mongo:
        print("✅ Conectado ao MongoDB")
        
        # Gera dados
        print("🔄 Gerando dados fictícios...")
        customers = generate_customers(1000)
        products = generate_products(500)
        orders = generate_orders(customers, products, 5000)
        
        # Insere no MongoDB
        db_name = "eshop_brasil"
        mongo[db_name].customers.insert_many(customers)
        mongo[db_name].products.insert_many(products)
        mongo[db_name].orders.insert_many(orders)
        
        print(f"✅ Dados inseridos no MongoDB:")
        print(f"   - {len(customers)} clientes")
        print(f"   - {len(products)} produtos")
        print(f"   - {len(orders)} pedidos")
    
    # Redis
    redis = db.connect_redis()
    if redis:
        print("✅ Conectado ao Redis")
        
        # Adiciona algumas métricas de cache
        redis.set("total_customers", len(customers))
        redis.set("total_products", len(products))
        redis.set("total_orders", len(orders))
        
        print("✅ Métricas básicas armazenadas no Redis")

if __name__ == "__main__":
    main()