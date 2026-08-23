-- Criação e configuração do banco de dados com charset UTF-8
CREATE DATABASE IF NOT EXISTS cadastro
DEFAULT CHARACTER SET utf8mb4
DEFAULT COLLATE utf8mb4_general_ci;

USE cadastro;

-- Criação da tabela 'pessoas' com constraints e Chave Primária
CREATE TABLE IF NOT EXISTS pessoas (
    id INT NOT NULL AUTO_INCREMENT,
    nome VARCHAR(30) NOT NULL,
    nascimento DATE,
    sexo ENUM('M', 'F'),
    peso DECIMAL(5,2),
    altura DECIMAL(3,2),
    nacionalidade VARCHAR(20) DEFAULT 'Brasil',
    PRIMARY KEY (id)
) DEFAULT CHARSET = utf8mb4;