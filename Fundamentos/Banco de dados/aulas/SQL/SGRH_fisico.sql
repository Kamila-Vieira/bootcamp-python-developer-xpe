CREATE TABLE funcionarios(
  funcionario_id int primary key,
  nome varchar(30),
  sobrenome varchar(50),
  salario decimal(8, 2),
  email varchar(50),
  data_admissao date,
  cargo_id int,
  departamento_id int,
);

CREATE UNIQUE INDEX ix_email_func ON funcionarios(email);

CREATE TABLE departamentos(
  departamento_id int primary key,
  departamento_nome varchar(50),
  regional_id int,
);


CREATE TABLE cargos(
  cargo_id int primary key,
  cargo_nome varchar(50),
);

CREATE TABLE cargo_historico(
  cargo_historico_id int primary key,
  data_inicio date,
  data_fim date,
  cargo_id int,
  funcionario_id int,
);

CREATE TABLE regionais(
  regional_id int primary key,
  estado varchar(30),
  cidade varchar(100),
  endereco varchar(3000),
  pais_id int,
);

CREATE TABLE paises(
  pais_id int primary key,
  pais_nome varchar(30),
  continente_id int,
);

CREATE TABLE continentes(
  continente_id int primary key,
  continente_nome varchar(30),
);

ALTER TABLE funcionarios ADD CONSTRAINT fk_func_dpto FOREIGN KEY(departamento_id) REFERENCES departamentos(departamento_id);
ALTER TABLE funcionarios ADD CONSTRAINT fk_func_cargo FOREIGN KEY(cargo_id) REFERENCES cargos(cargo_id);
ALTER TABLE cargo_historico ADD CONSTRAINT fk_ch_cargo FOREIGN KEY(cargo_id) REFERENCES cargos(cargo_id);
ALTER TABLE cargo_historico ADD CONSTRAINT fk_ch_func FOREIGN KEY(funcionario_id) REFERENCES funcionarios(funcionario_id);
ALTER TABLE departamentos ADD CONSTRAINT fk_depto_reg FOREIGN KEY(regional_id) REFERENCES regionais(regional_id);
ALTER TABLE regionais ADD CONSTRAINT fk_reg_pais FOREIGN KEY(pais_id) REFERENCES paises(pais_id);
ALTER TABLE paises ADD CONSTRAINT fk_pais_cont FOREIGN KEY(continente_id) REFERENCES continentes(continente_id);