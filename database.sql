DROP DATABASE IF EXISTS swim_towel_manager;
CREATE DATABASE swim_towel_manager
    DEFAULT CHARACTER SET utf8mb4
    DEFAULT COLLATE utf8mb4_unicode_ci;

USE swim_towel_manager;

-- ==========================================
-- 1. CRIAÇÃO DAS TABELAS
-- ==========================================

-- Tabela 1: ATENDENTE
CREATE TABLE atendente (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    cpf VARCHAR(14) NOT NULL UNIQUE,
    matricula VARCHAR(20) NOT NULL UNIQUE,
    email VARCHAR(150) NOT NULL UNIQUE
) ENGINE=InnoDB;

-- Tabela 2: NADADOR
CREATE TABLE nadador (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    cpf VARCHAR(14) NOT NULL UNIQUE,
    matricula VARCHAR(20) NOT NULL UNIQUE,
    telefone VARCHAR(20) NULL,
    status_cadastro VARCHAR(20) NOT NULL DEFAULT 'Ativo',
    CONSTRAINT chk_status_nadador CHECK (status_cadastro IN ('Ativo', 'Inativo', 'Suspenso'))
) ENGINE=InnoDB;

-- Tabela 3: TOALHA
CREATE TABLE toalha (
    id INT PRIMARY KEY AUTO_INCREMENT,
    codigo_barras VARCHAR(30) NOT NULL UNIQUE,
    tamanho VARCHAR(10) NOT NULL DEFAULT 'M',
    estado_conservacao VARCHAR(20) NOT NULL DEFAULT 'Novo',
    status_disponibilidade VARCHAR(20) NOT NULL DEFAULT 'Disponivel',
    CONSTRAINT chk_tamanho_toalha CHECK (tamanho IN ('P', 'M', 'G', 'GG', 'Infantil')),
    CONSTRAINT chk_estado_conservacao CHECK (estado_conservacao IN ('Novo', 'Bom', 'Desgastado', 'Danificado')),
    CONSTRAINT chk_status_disponibilidade CHECK (status_disponibilidade IN ('Disponivel', 'Em Uso', 'Em Lavagem', 'Perdida'))
) ENGINE=InnoDB;

-- Tabela 4: RETIRADA
CREATE TABLE retirada (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nadador_id INT NOT NULL,
    atendente_id INT NOT NULL,
    toalha_id INT NOT NULL,
    data_hora_retirada DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    data_hora_devolucao DATETIME NULL,
    status_emprestimo VARCHAR(20) NOT NULL DEFAULT 'Em Aberto',
    CONSTRAINT fk_retirada_nadador
        FOREIGN KEY (nadador_id) REFERENCES nadador(id)
        ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT fk_retirada_atendente
        FOREIGN KEY (atendente_id) REFERENCES atendente(id)
        ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT fk_retirada_toalha
        FOREIGN KEY (toalha_id) REFERENCES toalha(id)
        ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT chk_status_emprestimo CHECK (status_emprestimo IN ('Em Aberto', 'Devolvido', 'Atrasado', 'Perdido')),
    CONSTRAINT chk_datas_retirada CHECK (data_hora_devolucao IS NULL OR data_hora_devolucao >= data_hora_retirada)
) ENGINE=InnoDB;

-- Tabela 5: HISTORICO_TOALHA
CREATE TABLE historico_toalha (
    id INT PRIMARY KEY AUTO_INCREMENT,
    toalha_id INT NOT NULL,
    retirada_id INT NULL,
    data_evento DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    tipo_evento VARCHAR(30) NOT NULL,
    observacao VARCHAR(255) NULL,
    CONSTRAINT fk_historico_toalha
        FOREIGN KEY (toalha_id) REFERENCES toalha(id)
        ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT fk_historico_retirada
        FOREIGN KEY (retirada_id) REFERENCES retirada(id)
        ON DELETE SET NULL ON UPDATE CASCADE,
    CONSTRAINT chk_tipo_evento CHECK (tipo_evento IN ('Retirada', 'Devolucao', 'Envio Lavagem', 'Retorno Lavagem', 'Baixa Danificada', 'Perda Registrada'))
) ENGINE=InnoDB;

-- ==========================================
-- 2. INSERÇÃO DA MASSA DE DADOS (TOTAL: 1.000 REGISTROS)
-- ==========================================

-- 2.1 ATENDENTES (10 Registros)
INSERT INTO atendente (nome, cpf, matricula, email) VALUES
('Carlos Roberto Silva', '100.200.300-01', 'ATD001', 'carlos.roberto@escola.com'),
('Fernanda Lima Santos', '100.200.300-02', 'ATD002', 'fernanda.lima@escola.com'),
('Rodrigo Alves Costa', '100.200.300-03', 'ATD003', 'rodrigo.alves@escola.com'),
('Camila Rocha Xavier', '100.200.300-04', 'ATD004', 'camila.rocha@escola.com'),
('Lucas Mendes Faria', '100.200.300-05', 'ATD005', 'lucas.mendes@escola.com'),
('Beatriz Costa Ramos', '100.200.300-06', 'ATD006', 'beatriz.costa@escola.com'),
('Gabriel Santos Paiva', '100.200.300-07', 'ATD007', 'gabriel.santos@escola.com'),
('Juliana Paes Freitas', '100.200.300-08', 'ATD008', 'juliana.paes@escola.com'),
('Marcelo Oliveira Vaz', '100.200.300-09', 'ATD009', 'marcelo.oliveira@escola.com'),
('Patricia Ramos Nogueira', '100.200.300-10', 'ATD100', 'patricia.ramos@escola.com');

-- 2.2 NADADORES (150 Registros)
INSERT INTO nadador (nome, cpf, matricula, telefone, status_cadastro) VALUES
('Ana Silva', '200.300.400-01', 'NAD001', '(84) 98888-0001', 'Ativo'),
('Bruno Souza', '200.300.400-02', 'NAD002', '(84) 98888-0002', 'Ativo'),
('Carla Dias', '200.300.400-03', 'NAD003', '(84) 98888-0003', 'Ativo'),
('Diego Ferreira', '200.300.400-04', 'NAD004', '(84) 98888-0004', 'Ativo'),
('Eduarda Martins', '200.300.400-05', 'NAD005', '(84) 98888-0005', 'Inativo'),
('Felipe Andrade', '200.300.400-06', 'NAD006', '(84) 98888-0006', 'Ativo'),
('Gabriela Melo', '200.300.400-07', 'NAD007', '(84) 98888-0007', 'Ativo'),
('Heitor Castro', '200.300.400-08', 'NAD008', '(84) 98888-0008', 'Suspenso'),
('Isabela Rocha', '200.300.400-09', 'NAD009', '(84) 98888-0009', 'Ativo'),
('João Pedro Ribeiro', '200.300.400-10', 'NAD010', '(84) 98888-0010', 'Ativo'),
('Kauan Carvalho', '200.300.400-11', 'NAD011', '(84) 98888-0011', 'Ativo'),
('Lara Lima', '200.300.400-12', 'NAD012', '(84) 98888-0012', 'Ativo'),
('Mateus Silveira', '200.300.400-13', 'NAD013', '(84) 98888-0013', 'Inativo'),
('Natalia Farias', '200.300.400-14', 'NAD014', '(84) 98888-0014', 'Ativo'),
('Otavio Fonseca', '200.300.400-15', 'NAD015', '(84) 98888-0015', 'Ativo'),
('Paula Mendes', '200.300.400-16', 'NAD016', '(84) 98888-0016', 'Ativo'),
('Quintino Neto', '200.300.400-17', 'NAD017', '(84) 98888-0017', 'Ativo'),
('Rafaela Aguiar', '200.300.400-18', 'NAD018', '(84) 98888-0018', 'Ativo'),
('Samuel Nogueira', '200.300.400-19', 'NAD019', '(84) 98888-0019', 'Ativo'),
('Tatiane Franco', '200.300.400-20', 'NAD020', '(84) 98888-0020', 'Suspenso'),
('Uriel Barbosa', '200.300.400-21', 'NAD021', '(84) 98888-0021', 'Ativo'),
('Vanessa Guimarães', '200.300.400-22', 'NAD022', '(84) 98888-0022', 'Ativo'),
('William Xavier', '200.300.400-23', 'NAD023', '(84) 98888-0023', 'Ativo'),
('Yara Campos', '200.300.400-24', 'NAD024', '(84) 98888-0024', 'Ativo'),
('Zeca Pagodinho', '200.300.400-25', 'NAD025', '(84) 98888-0025', 'Inativo');

-- Procedimento temporário para completar a lista de 150 Nadadores
DELIMITER $$
CREATE PROCEDURE PopulaNadadores()
BEGIN
    DECLARE i INT DEFAULT 26;
    WHILE i <= 150 DO
        INSERT INTO nadador (nome, cpf, matricula, telefone, status_cadastro)
        VALUES (
            CONCAT('Nadador Teste ', i),
            CONCAT('200.300.400-', LPAD(i, 2, '0')),
            CONCAT('NAD', LPAD(i, 3, '0')),
            CONCAT('(84) 98888-', LPAD(i, 4, '0')),
            IF(i % 10 = 0, 'Inativo', 'Ativo')
        );
        SET i = i + 1;
    END WHILE;
END$$
DELIMITER ;
CALL PopulaNadadores();
DROP PROCEDURE PopulaNadadores;

-- 2.3 TOALHAS (240 Registros)
DELIMITER $$
CREATE PROCEDURE PopulaToalhas()
BEGIN
    DECLARE i INT DEFAULT 1;
    DECLARE tam VARCHAR(10);
    DECLARE est VARCHAR(20);
    DECLARE disp VARCHAR(20);

    WHILE i <= 240 DO
        -- Alternando tamanhos
        CASE (i % 5)
            WHEN 0 THEN SET tam = 'Infantil';
            WHEN 1 THEN SET tam = 'P';
            WHEN 2 THEN SET tam = 'M';
            WHEN 3 THEN SET tam = 'G';
            ELSE SET tam = 'GG';
        END CASE;

        -- Alternando conservação
        CASE (i % 4)
            WHEN 0 THEN SET est = 'Desgastado';
            WHEN 1 THEN SET est = 'Novo';
            WHEN 2 THEN SET est = 'Bom';
            ELSE SET est = 'Novo';
        END CASE;

        -- Alternando disponibilidade
        CASE (i % 6)
            WHEN 0 THEN SET disp = 'Em Lavagem';
            WHEN 1 THEN SET disp = 'Em Uso';
            ELSE SET disp = 'Disponivel';
        END CASE;

        INSERT INTO toalha (codigo_barras, tamanho, estado_conservacao, status_disponibilidade)
        VALUES (
            CONCAT('TLH-2026-', LPAD(i, 3, '0')),
            tam,
            est,
            disp
        );
        SET i = i + 1;
    END WHILE;
END$$
DELIMITER ;
CALL PopulaToalhas();
DROP PROCEDURE PopulaToalhas;

-- 2.4 RETIRADAS (300 Registros)
DELIMITER $$
CREATE PROCEDURE PopulaRetiradas()
BEGIN
    DECLARE i INT DEFAULT 1;
    DECLARE nad_id INT;
    DECLARE atd_id INT;
    DECLARE tlh_id INT;
    DECLARE st VARCHAR(20);
    DECLARE dt_ret DATETIME;
    DECLARE dt_dev DATETIME;

    WHILE i <= 300 DO
        SET nad_id = ((i - 1) % 150) + 1;
        SET atd_id = ((i - 1) % 10) + 1;
        SET tlh_id = ((i - 1) % 240) + 1;
        SET dt_ret = DATE_ADD('2026-09-01 08:00:00', INTERVAL i HOUR);

        IF (i % 4 = 0) THEN
            -- Empréstimo em aberto
            SET st = 'Em Aberto';
            SET dt_dev = NULL;
        ELSE
            -- Devolvido
            SET st = 'Devolvido';
            SET dt_dev = DATE_ADD(dt_ret, INTERVAL 1 HOUR);
        END IF;

        INSERT INTO retirada (nadador_id, atendente_id, toalha_id, data_hora_retirada, data_hora_devolucao, status_emprestimo)
        VALUES (nad_id, atd_id, tlh_id, dt_ret, dt_dev, st);

        SET i = i + 1;
    END WHILE;
END$$
DELIMITER ;
CALL PopulaRetiradas();
DROP PROCEDURE PopulaRetiradas;

-- 2.5 HISTORICO_TOALHA (300 Registros)
DELIMITER $$
CREATE PROCEDURE PopulaHistorico()
BEGIN
    DECLARE i INT DEFAULT 1;
    DECLARE tlh_id INT;
    DECLARE ret_id INT;
    DECLARE ev VARCHAR(30);
    DECLARE obs VARCHAR(255);
    DECLARE dt_ev DATETIME;

    WHILE i <= 300 DO
        SET tlh_id = ((i - 1) % 240) + 1;
        SET ret_id = i;
        SET dt_ev = DATE_ADD('2026-09-01 08:00:00', INTERVAL i HOUR);

        IF (i % 2 = 1) THEN
            SET ev = 'Retirada';
            SET obs = 'Toalha retirada na recepção pelo aluno';
        ELSE
            SET ev = 'Devolucao';
            SET obs = 'Toalha devolvida em bom estado para recepção';
        END IF;

        INSERT INTO historico_toalha (toalha_id, retirada_id, data_evento, tipo_evento, observacao)
        VALUES (tlh_id, ret_id, dt_ev, ev, obs);

        SET i = i + 1;
    END WHILE;
END$$
DELIMITER ;
CALL PopulaHistorico();
DROP PROCEDURE PopulaHistorico;