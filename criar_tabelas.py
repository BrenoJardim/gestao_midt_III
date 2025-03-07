import sqlite3

# Conecta-se ao banco de dados ou o cria se não existir
conn = sqlite3.connect('erp.db')
cursor = conn.cursor()

# Cria a tabela de Clientes
cursor.execute('''CREATE TABLE IF NOT EXISTS clientes (
                    id INTEGER PRIMARY KEY,
                    nome TEXT NOT NULL,
                    telefone TEXT,
                    endereco TEXT
                    )''')

# Cria a tabela de Fornecedores
cursor.execute('''CREATE TABLE IF NOT EXISTS fornecedores (
                    id INTEGER PRIMARY KEY,
                    nome TEXT NOT NULL,
                    telefone TEXT,
                    endereco TEXT
                    )''')

# Cria a tabela de Produtos
cursor.execute('''CREATE TABLE IF NOT EXISTS produtos (
                    id INTEGER PRIMARY KEY,
                    nome TEXT NOT NULL,
                    codigo TEXT NOT NULL,
                    custo REAL,
                    valor_venda REAL,
                    tipo_medida TEXT,
                    estoque INTEGER DEFAULT 0  -- Adiciona a coluna estoque com valor padrão 0
                    )''')

# Cria a tabela de Adições do Sítio
cursor.execute('''CREATE TABLE IF NOT EXISTS adicoes_sitio (
                    id INTEGER PRIMARY KEY,
                    produto_id INTEGER,
                    nome_produto INTEGER,
                    quantidade INTEGER,
                    data_adicao DATE
                    )''')

# Cria a tabela para registrar as transações financeiras
cursor.execute('''CREATE TABLE IF NOT EXISTS transacoes (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        data TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        valor REAL,
                        debito BOOLEAN,
                        credito BOOLEAN,
                        avista BOOLEAN,
                        pix BOOLEAN,
                        a_combinar BOOLEAN,
                        fluxo_caixa TEXT
                    )''')

# Cria a tabela para registrar as compras
cursor.execute('''CREATE TABLE IF NOT EXISTS compras (
                        id_compra INTEGER PRIMARY KEY,
                        fornecedor TEXT NOT NULL,
                        data TEXT NOT NULL,
                        desconto DECIMAL(10, 2),
                        forma_pagamento TEXT NOT NULL,
                        valor_final DECIMAL(10, 2)
                    )''')

# Cria a tabela para registrar as compras
cursor.execute('''CREATE TABLE IF NOT EXISTS compras_produtos (
                        id_compra INT,
                        id_produto INT,
                        nome_produto VARCHAR(255),
                        quantidade INT,
                        custo_unitario DECIMAL(10, 2),
                        valor_total DECIMAL(10, 2),
                        FOREIGN KEY (id_compra) REFERENCES compras(id),
                        FOREIGN KEY (id_produto) REFERENCES produtos(id)
                    )''')



# Cria a tabela para registrar o registro financeiro
cursor.execute('''CREATE TABLE IF NOT EXISTS registro_financeiro (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        tipo VARCHAR(20) NOT NULL,
                        descricao TEXT NOT NULL,
                        valor REAL NOT NULL,
                        pagamento TEXT NOT NULL,
                        data TEXT
                    )''')

# Criando a tabela de usuários
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT UNIQUE NOT NULL,
                        password TEXT NOT NULL
                    )''')

# Criar a tabela de vendas
cursor.execute('''CREATE TABLE IF NOT EXISTS vendas (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        data DATE,
                        cliente TEXT,
                        produto TEXT,
                        quantidade INTEGER,
                        valor_venda REAL,
                        desconto REAL,
                        total REAL,
                        forma_pagamento TEXT,
                        lucro REAL
                    )''')

# Criando a tabela de Configurações
cursor.execute('''CREATE TABLE IF NOT EXISTS configuracoes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    chave TEXT UNIQUE NOT NULL CHECK(length(chave) > 0),
                    valor TEXT NOT NULL
                )''')

# Salva as alterações e fecha a conexão
conn.commit()
conn.close()
