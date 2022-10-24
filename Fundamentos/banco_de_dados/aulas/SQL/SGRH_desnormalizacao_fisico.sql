
CREATE TABLE continentes (
                continente_id INT NOT NULL,
                continente_nome VARCHAR(30) NOT NULL,
                CONSTRAINT pk_continentes PRIMARY KEY (continente_id)
)

CREATE TABLE paises (
                pais_id INT NOT NULL,
                pais_nome VARCHAR(30) NOT NULL,
                continente_id INT NOT NULL,
                CONSTRAINT pk_paises PRIMARY KEY (pais_id)
)

CREATE TABLE regionais (
                regional_id INT NOT NULL,
                estado VARCHAR(30) NOT NULL,
                cidade VARCHAR(100) NOT NULL,
                endereco VARCHAR(3000) NOT NULL,
                pais_id INT NOT NULL,
                CONSTRAINT pk_regionais PRIMARY KEY (regional_id)
)

CREATE TABLE cargos (
                cargo_id INT NOT NULL,
                cargo_nome VARCHAR(50) NOT NULL,
                CONSTRAINT pk_cargos PRIMARY KEY (cargo_id)
)

CREATE TABLE funcionarios (
                funcionario_id INT NOT NULL,
                nome VARCHAR(30) NOT NULL,
                sobrenome VARCHAR(50),
                data_admissao DATETIME NOT NULL,
                email VARCHAR(50) NOT NULL,
                salario NUMERIC(8,2) NOT NULL,
                cargo_id INT NOT NULL,
                departamento_id INT NOT NULL,
                departamento_nome VARCHAR(50) NOT NULL,
                regional_id INT NOT NULL,
                CONSTRAINT pk_funcionarios PRIMARY KEY (funcionario_id)
)
CREATE UNIQUE  CLUSTERED INDEX idx_func_email
 ON funcionarios
 ( email )

CREATE  NONCLUSTERED INDEX idx_depto_func
 ON funcionarios
 ( departamento_id, departamento_nome, regional_id )


CREATE TABLE cargo_historico (
                cargo_historico_id INT NOT NULL,
                data_fim DATETIME NOT NULL,
                data_inicio DATETIME NOT NULL,
                cargo_id INT NOT NULL,
                funcionario_id INT NOT NULL,
                CONSTRAINT pk_cargo_historico PRIMARY KEY (cargo_historico_id)
)

ALTER TABLE paises ADD CONSTRAINT continentes_paises_fk
FOREIGN KEY (continente_id)
REFERENCES continentes (continente_id)
ON DELETE NO ACTION
ON UPDATE NO ACTION

ALTER TABLE regionais ADD CONSTRAINT paises_regionais_fk
FOREIGN KEY (pais_id)
REFERENCES paises (pais_id)
ON DELETE NO ACTION
ON UPDATE NO ACTION

ALTER TABLE funcionarios ADD CONSTRAINT regionais_funcionarios_fk
FOREIGN KEY (regional_id)
REFERENCES regionais (regional_id)
ON DELETE NO ACTION
ON UPDATE NO ACTION

ALTER TABLE funcionarios ADD CONSTRAINT cargos_funcionarios_fk
FOREIGN KEY (cargo_id)
REFERENCES cargos (cargo_id)
ON DELETE NO ACTION
ON UPDATE NO ACTION

ALTER TABLE cargo_historico ADD CONSTRAINT cargos_cargo_historico_fk
FOREIGN KEY (cargo_id)
REFERENCES cargos (cargo_id)
ON DELETE NO ACTION
ON UPDATE NO ACTION

ALTER TABLE cargo_historico ADD CONSTRAINT funcionarios_cargo_historico_fk
FOREIGN KEY (funcionario_id)
REFERENCES funcionarios (funcionario_id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
