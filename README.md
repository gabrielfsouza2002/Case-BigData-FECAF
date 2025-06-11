# Aplicação Prática de Tecnologias de Banco de Dados e Big Data em uma Empresa de Comércio Eletrônico: E-Shop Brasil

## Introdução

Este projeto visa resolver desafios críticos de gestão de dados e otimização logística enfrentados pela **E-Shop Brasil**, uma das maiores plataformas de comércio eletrônico do país. Com milhões de clientes ativos e centenas de milhares de pedidos diários, a empresa necessita de soluções inovadoras que garantam a segurança dos dados, personalizem a experiência do cliente e otimizem a cadeia de suprimentos.

Nossa missão é propor e demonstrar, de forma prática e visual, como a E-Shop Brasil pode superar esses desafios utilizando tecnologias avançadas de bancos de dados relacionais (embora o foco aqui seja NoSQL para flexibilidade), NoSQL e conceitos de Big Data. A solução foca em uma arquitetura escalável e integrada, essencial para o crescimento e sustentabilidade a longo prazo da empresa.

### Objetivos do Projeto

*   **Garantir a Segurança e Privacidade dos Dados:** Assegurar a proteção das informações pessoais e financeiras dos clientes, em conformidade com regulamentações como a LGPD.
*   **Personalizar a Experiência do Cliente:** Desenvolver a capacidade de coletar, armazenar e analisar dados de comportamento para oferecer recomendações e navegação altamente personalizadas.
*   **Otimizar a Logística:** Melhorar a eficiência da entrega e do controle de estoques, com foco em regiões distantes, e integrar operações omnichannel.
*   **Demonstrar Escalabilidade e Integração:** Utilizar tecnologias que permitam o processamento de grandes volumes de dados e a fácil integração entre diferentes sistemas.

## Descrição do Projeto

Este projeto apresenta uma aplicação web interativa desenvolvida em **Streamlit**, que se conecta a um banco de dados **MongoDB** (um banco NoSQL). Todo o ambiente é orquestrado via **Docker** e **Docker Compose**, garantindo um ambiente de desenvolvimento e execução isolado e padronizado.

A aplicação `app.py` simula operações essenciais de uma plataforma de e-commerce, demonstrando como dados de clientes, produtos e pedidos podem ser gerenciados, visualizados e utilizados para análises básicas que simulam o potencial do Big Data na melhoria da experiência do cliente e na eficiência operacional.

### Tecnologias Utilizadas

*   **Python:** Linguagem de programação principal.
*   **Streamlit:** Framework para criação rápida de aplicações web interativas.
*   **MongoDB:** Banco de dados NoSQL orientado a documentos, escolhido por sua flexibilidade e escalabilidade para lidar com dados semi-estruturados e não estruturados (e.g., logs de navegação, perfis de usuários com atributos variáveis).
*   **Docker e Docker Compose:** Para conteinerização e orquestração dos serviços.
*   **PyMongo:** Driver Python para MongoDB.
*   **Faker:** Biblioteca para geração de dados fictícios para testes.
*   **Pandas:** Para manipulação e análise de dados.

### Componentes da Solução

1.  **Ambiente Dockerizado:** Um `docker-compose.yml` configura um serviço MongoDB, facilitando a inicialização do banco de dados.
2.  **Aplicação Streamlit (`app.py`):**
    *   **Conexão ao MongoDB:** Estabelece a comunicação com o banco de dados.
    *   **Geração de Dados Iniciais:** Funcionalidade para popular o banco com dados de exemplo (clientes, produtos, pedidos) para facilitar testes e demonstrações.
    *   **Operações CRUD:** Permite a inserção, visualização, edição e exclusão de dados.
    *   **Análises Simplificadas:** Demonstra a capacidade de combinar dados de diferentes coleções para gerar insights (e.g., listagem de clientes e seus pedidos mais recentes).

## Passos para Implementação

Siga as instruções abaixo para configurar e executar o ambiente do projeto.

### Pré-requisitos

Certifique-se de ter o Docker e o Docker Compose instalados em sua máquina.

*   [Instalar Docker Desktop](https://www.docker.com/products/docker-desktop/)

### 1. Clonar o Repositório

```bash
git clone <URL_DO_SEU_REPOSITORIO_GITHUB>
cd <nome_do_seu_repositorio>
```

### 2. Subir a Infraestrutura com Docker Compose

Dentro do diretório do projeto, execute o comando para iniciar o serviço do MongoDB:

```bash
docker-compose up -d
```
Este comando irá baixar a imagem do MongoDB (se ainda não tiver), criar e iniciar o container mongodb_eshop em segundo plano

### 3. Instalar Dependências do Python
É recomendado criar um ambiente virtual para o projeto:

```bash
python -m venv venv
source venv/bin/activate  # No Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```
Crie o arquivo requirements.txt com o seguinte conteúdo:

streamlit
pymongo
pandas
Faker


### 4. Executar a Aplicação Streamlit

Com o ambiente virtual ativado e as dependências instaladas, execute a aplicação Streamlit:

```bash
streamlit run app.py
```
Após executar o comando, o Streamlit irá abrir automaticamente a aplicação em seu navegador padrão (geralmente em http://localhost:8501).


## Funcionalidades da Aplicação (app.py)

A aplicação Streamlit oferece as seguintes funcionalidades principais:

*   **Geração de Dados Iniciais:** Preenche o MongoDB com dados fictícios de clientes, produtos e pedidos para simular um cenário real. Isso é útil para começar a trabalhar rapidamente.
*   **Inserção de Dados:** Formulários simples para adicionar novos registros nas coleções de clientes e produtos.
*   **Visualização de Dados:** Exibe os dados de clientes, produtos e pedidos em tabelas interativas.
*   **Manipulação de Dados:** Permite buscar registros por ID e, em seguida, editá-los ou excluí-los, demonstrando a capacidade de atualização do banco de dados.
*   **Análises & Concatenação:** Apresenta exemplos de como dados de diferentes coleções podem ser combinados (concatenados) para gerar insights. Por exemplo, você poderá ver uma lista de clientes com seus pedidos mais recentes, ou os produtos mais vendidos. Isso simula o potencial do Big Data para cruzar informações e melhorar a compreensão do negócio.

## Testes e Exemplos

A pasta exemplos/ contém capturas de tela (prints) ou GIFs animados que demonstrem as funcionalidades da aplicação em ação.
