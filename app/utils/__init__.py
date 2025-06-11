# app/utils/__init__.py

"""
Módulo de utilitários para a aplicação E-Shop Brasil Analytics.
Contém funções auxiliares para geração de dados e conexão com bancos.
"""

# Importar as classes ou funções que você quer expor diretamente quando 'utils' for importado
from .data_generator import generate_customers, generate_products, generate_orders
from .database import DatabaseConnector