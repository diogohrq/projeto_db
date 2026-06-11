-- =============================================
-- CRIAÇÃO DAS TABELAS
-- =============================================

-- Tabela categoria
CREATE TABLE categoria (
    id INTEGER PRIMARY KEY NOT NULL,
    nome VARCHAR(255) NOT NULL UNIQUE
);

-- Tabela marca
CREATE TABLE marca (
    id INTEGER PRIMARY KEY NOT NULL,
    nome VARCHAR(255) NOT NULL
);

-- Tabela produto
CREATE TABLE produto (
    id INTEGER PRIMARY KEY NOT NULL,
    nome VARCHAR(255) NOT NULL,
    preco DECIMAL(10, 2) NOT NULL CHECK (preco > 0),
    id_categoria INTEGER REFERENCES categoria(id),
    id_marca INTEGER REFERENCES marca(id)
);

-- Tabela estoque
CREATE TABLE estoque (
    id INTEGER PRIMARY KEY NOT NULL,
    id_produto INTEGER UNIQUE REFERENCES produto(id),
    quantidade INTEGER NOT NULL DEFAULT 0 CHECK (quantidade >= 0)
);

-- Tabela movimentacao
CREATE TABLE movimentacao (
    id INTEGER PRIMARY KEY NOT NULL,
    id_produto INTEGER REFERENCES produto(id),
    tipo VARCHAR(50) NOT NULL CHECK (tipo IN ('ENTRADA', 'SAIDA')),
    quantidade INTEGER NOT NULL CHECK (quantidade > 0),
    data DATE DEFAULT CURRENT_DATE
);