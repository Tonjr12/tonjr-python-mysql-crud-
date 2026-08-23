-- EXERCÍCIO 1: Produtos
CREATE DATABASE IF NOT EXISTS loja_db;
USE loja_db;

CREATE TABLE IF NOT EXISTS produtos (
    id INT AUTO_INCREMENT NOT NULL,
    nome VARCHAR(50) NOT NULL,
    descricao VARCHAR(255),
    preco DECIMAL(6,2) NOT NULL,
    categoria ENUM('Eletronicos', 'Vestuario', 'Alimentos'),
    estoque INT DEFAULT 0,
    PRIMARY KEY (id)
);

-- EXERCÍCIO 2: Veículos
CREATE DATABASE IF NOT EXISTS garagem_db;
USE garagem_db;

CREATE TABLE IF NOT EXISTS veiculos (
    id INT NOT NULL AUTO_INCREMENT,
    placa VARCHAR(30) NOT NULL,
    modelo VARCHAR(30) NOT NULL,
    marca VARCHAR(30) NOT NULL,
    ano_fabricacao YEAR,
    combustivel ENUM('Flex', 'Gasolina', 'Etanol', 'Diesel', 'Eletrico') DEFAULT 'Flex',
    PRIMARY KEY (id)
);

-- EXERCÍCIO 3: Alunos
CREATE DATABASE IF NOT EXISTS escola_db;
USE escola_db;

CREATE TABLE IF NOT EXISTS alunos (
    matricula INT NOT NULL AUTO_INCREMENT,
    nome VARCHAR(40) NOT NULL,
    data_nascimento DATE,
    mensalidade DECIMAL(6,2),
    situacao ENUM('ativo', 'inativo', 'trancado') DEFAULT 'ativo',
    PRIMARY KEY (matricula)
);