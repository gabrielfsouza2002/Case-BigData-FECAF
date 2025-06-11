from faker import Faker
import random
from datetime import datetime, timedelta
import pandas as pd

fake = Faker('pt_BR')

def generate_customers(n=1000):
    """Gera dados fictícios de clientes"""
    customers = []
    for _ in range(n):
        customer = {
            'customer_id': fake.uuid4(),
            'name': fake.name(),
            'email': fake.email(),
            'phone': fake.phone_number(),
            'city': fake.city(),
            'state': fake.state_abbr(),
            'registration_date': fake.date_between(
                start_date='-2y', 
                end_date='today'
            )
        }
        customers.append(customer)
    return customers

def generate_products(n=500):
    """Gera dados fictícios de produtos"""
    categories = ['Eletrônicos', 'Moda', 'Casa', 'Esportes', 'Livros']
    products = []
    for _ in range(n):
        product = {
            'product_id': fake.uuid4(),
            'name': fake.catch_phrase(),
            'category': random.choice(categories),
            'price': round(random.uniform(10, 5000), 2),
            'stock': random.randint(0, 1000)
        }
        products.append(product)
    return products

def generate_orders(customers, products, n=5000):
    """Gera dados fictícios de pedidos"""
    orders = []
    for _ in range(n):
        order = {
            'order_id': fake.uuid4(),
            'customer_id': random.choice(customers)['customer_id'],
            'product_id': random.choice(products)['product_id'],
            'quantity': random.randint(1, 5),
            'order_date': fake.date_time_between(
                start_date='-1y', 
                end_date='now'
            ),
            'status': random.choice(['Pendente', 'Processando', 'Enviado', 'Entregue'])
        }
        orders.append(order)
    return orders