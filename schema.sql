-- =============================================
-- CRIAÇÃO DAS TABELAS
-- =============================================

SET NAMES utf8mb4;
SET CHARACTER SET utf8mb4;

-- Tabela categoria
CREATE TABLE categoria (
  id INTEGER PRIMARY KEY NOT NULL,
  nome VARCHAR(255) NOT NULL UNIQUE
) CHARACTER SET utf8mb4;

-- Tabela marca
CREATE TABLE marca (
  id INTEGER PRIMARY KEY NOT NULL,
  nome VARCHAR(255) NOT NULL
) CHARACTER SET utf8mb4;

-- Tabela produto
CREATE TABLE produto (
  id INTEGER PRIMARY KEY NOT NULL,
  nome VARCHAR(255) NOT NULL,
  preco DECIMAL(10, 2) NOT NULL CHECK (preco > 0),
  id_categoria INTEGER,
  id_marca INTEGER,
  FOREIGN KEY (id_categoria) REFERENCES categoria(id),
  FOREIGN KEY (id_marca) REFERENCES marca(id)
) CHARACTER SET utf8mb4;

-- Tabela estoque
CREATE TABLE estoque (
  id INTEGER PRIMARY KEY NOT NULL,
  id_produto INTEGER UNIQUE,
  quantidade INTEGER NOT NULL DEFAULT 0 CHECK (quantidade >= 0),
  FOREIGN KEY (id_produto) REFERENCES produto(id)
) CHARACTER SET utf8mb4;

-- Tabela movimentacao
CREATE TABLE movimentacao (
  id INTEGER PRIMARY KEY NOT NULL,
  id_produto INTEGER,
  tipo VARCHAR(50) NOT NULL CHECK (tipo IN ('ENTRADA', 'SAIDA')),
  quantidade INTEGER NOT NULL CHECK (quantidade > 0),
  data DATE NULL,
  FOREIGN KEY (id_produto) REFERENCES produto(id)
) CHARACTER SET utf8mb4;

-- =============================================
-- INSERTS (DADOS DE EXEMPLO)
-- =============================================

-- Inserindo categorias
INSERT INTO categoria (id, nome) VALUES
(1, 'Bebidas'),
(2, 'Alimentos'),
(3, 'Hortifrúti'),
(4, 'Limpeza'),
(5, 'Higiene Pessoal'),
(6, 'Laticínios'),
(7, 'Padaria');

-- Inserindo marcas
INSERT INTO marca (id, nome) VALUES
(1, 'Coca-Cola'),
(2, 'Nestlé'),
(3, 'P&G'),
(4, 'Unilever'),
(5, 'Itambé'),
(6, 'Piraquê'),
(7, 'Sadia'),
(8, 'Omo'),
(9, 'Dove'),
(10, 'Heineken');

-- Inserindo produtos
INSERT INTO produto (id, nome, preco, id_categoria, id_marca) VALUES
(1, 'Coca-Cola 2L', 8.99, 1, 1),
(2, 'Água Mineral 500ml', 2.50, 1, 2),
(3, 'Suco Del Valle Laranja 1L', 6.90, 1, 2),
(4, 'Arroz Integral 5kg', 24.90, 2, 2),
(5, 'Feijão Carioca 1kg', 7.50, 2, 7),
(6, 'Macarrão Espaguete 500g', 4.29, 2, 6),
(7, 'Banana Prata kg', 5.99, 3, NULL),
(8, 'Maçã Fuji kg', 8.90, 3, NULL),
(9, 'Alface Americana', 3.50, 3, NULL),
(10, 'Detergente Ypê 500ml', 2.29, 4, 4),
(11, 'Água Sanitária 1L', 4.50, 4, 4),
(12, 'Sabão em Pó Omo 1kg', 12.90, 4, 8),
(13, 'Shampoo Dove 350ml', 15.90, 5, 9),
(14, 'Sabonete Dove 90g', 2.49, 5, 9),
(15, 'Leite Integral 1L', 5.49, 6, 5),
(16, 'Iogurte Grego 170g', 4.99, 6, 5),
(17, 'Queijo Mussarela 500g', 24.90, 6, 5),
(18, 'Pão Francês (6 unid)', 5.00, 7, 6),
(19, 'Cerveja Heineken 350ml', 4.99, 1, 10),
(20, 'Presunto Sadia 300g', 12.90, 2, 7);

-- Inserindo estoque inicial
INSERT INTO estoque (id, id_produto, quantidade) VALUES
(1, 1, 50),
(2, 2, 200),
(3, 3, 30),
(4, 4, 25),
(5, 5, 40),
(6, 6, 100),
(7, 7, 80),
(8, 8, 60),
(9, 9, 45),
(10, 10, 150),
(11, 11, 75),
(12, 12, 35),
(13, 13, 20),
(14, 14, 200),
(15, 15, 90),
(16, 16, 65),
(17, 17, 30),
(18, 18, 120),
(19, 19, 150),
(20, 20, 45);

-- Inserindo movimentações de exemplo
INSERT INTO movimentacao (id, id_produto, tipo, quantidade, data) VALUES
-- Entradas (compras/reposições)
(1, 1, 'ENTRADA', 100, '2024-01-10'),
(2, 2, 'ENTRADA', 300, '2024-01-12'),
(3, 4, 'ENTRADA', 50, '2024-01-15'),
(4, 10, 'ENTRADA', 200, '2024-01-18'),
(5, 15, 'ENTRADA', 100, '2024-01-20'),
(6, 19, 'ENTRADA', 200, '2024-01-22'),

-- Saídas (vendas)
(7, 1, 'SAIDA', 30, '2024-01-11'),
(8, 2, 'SAIDA', 80, '2024-01-13'),
(9, 3, 'SAIDA', 15, '2024-01-14'),
(10, 5, 'SAIDA', 10, '2024-01-15'),
(11, 7, 'SAIDA', 25, '2024-01-16'),
(12, 10, 'SAIDA', 40, '2024-01-17'),
(13, 14, 'SAIDA', 50, '2024-01-18'),
(14, 16, 'SAIDA', 20, '2024-01-19'),
(15, 18, 'SAIDA', 60, '2024-01-20'),
(16, 1, 'SAIDA', 20, '2024-01-21'),
(17, 19, 'SAIDA', 50, '2024-01-22'),
(18, 4, 'SAIDA', 10, '2024-01-23'),
(19, 12, 'SAIDA', 15, '2024-01-24'),
(20, 20, 'SAIDA', 5, '2024-01-25');