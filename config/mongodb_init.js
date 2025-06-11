// config/mongodb_init.js

// Script de inicialização para o MongoDB (executado na primeira vez que o container é criado)

// Cria o banco de dados e as coleções se não existirem
db = db.getSiblingDB('eshop_db');

// Cria coleções explicitamente (opcional, pois elas são criadas na primeira inserção)
db.createCollection("clientes");
db.createCollection("produtos");
db.createCollection("pedidos");

// Cria índices para otimização de queries
db.clientes.createIndex({ "email": 1 }, { unique: true });
db.produtos.createIndex({ "categoria": 1 });
db.produtos.createIndex({ "nome": "text" }); // Índice de texto para busca
db.pedidos.createIndex({ "cliente_id": 1 });
db.pedidos.createIndex({ "data_pedido": -1 }); // Índice para ordenar por data do pedido

if (db.clientes.countDocuments({}) === 0) {
    print("Inserindo dados iniciais de exemplo no MongoDB...");
    db.clientes.insertMany([
        { "nome": "João Silva", "email": "joao.silva@example.com", "endereco": "Rua A, 123", "telefone": "11987654321", "data_cadastro": new Date() },
        { "nome": "Maria Souza", "email": "maria.souza@example.com", "endereco": "Av. B, 456", "telefone": "21998765432", "data_cadastro": new Date() }
    ]);
    db.produtos.insertMany([
        { "nome": "Smartphone X", "descricao": "Um smartphone avançado.", "preco": 1999.99, "categoria": "Eletrônicos", "estoque": 100 },
        { "nome": "Camiseta Algodão", "descricao": "Camiseta básica de algodão.", "preco": 59.90, "categoria": "Moda", "estoque": 500 }
    ]);
    print("Dados iniciais inseridos.");
} else {
    print("Banco de dados já contém dados. Nenhuma inserção inicial executada.");
}

print("Configuração inicial do MongoDB concluída.");