
CREATE TABLE tb_aeronave (
                num_aeronave NUMBER NOT NULL,
                nm_aeronave VARCHAR2(50) NOT NULL,
                CONSTRAINT PK_AERONAVE PRIMARY KEY (num_aeronave)
);


CREATE TABLE tb_cidade (
                num_cidade NUMBER NOT NULL,
                nm_cidade VARCHAR2(50) NOT NULL,
                CONSTRAINT PK_CIDADE PRIMARY KEY (num_cidade)
);


CREATE TABLE tb_funcionario (
                num_funcionario NUMBER NOT NULL,
                ds_cpf VARCHAR2(11) NOT NULL,
                nm_fucionario VARCHAR2(50) NOT NULL,
                CONSTRAINT PK_FUNCIONARIO PRIMARY KEY (num_funcionario)
);


CREATE UNIQUE INDEX idx_cpf
 ON tb_funcionario
 ( ds_cpf );

CREATE TABLE tb_voos (
                num_voo NUMBER NOT NULL,
                dt_data_voo DATE NOT NULL,
                num_cidade_origem NUMBER NOT NULL,
                num_cidade_destino NUMBER NOT NULL,
                num_aeronave NUMBER NOT NULL,
                CONSTRAINT PK_VOO PRIMARY KEY (num_voo)
);
COMMENT ON COLUMN tb_voos.dt_data_voo IS 'Data do voo.';
COMMENT ON COLUMN tb_voos.num_cidade_origem IS 'Cidade que origina os voos da cia.';
COMMENT ON COLUMN tb_voos.num_cidade_destino IS 'Cidade que destina os voos da cia.';
COMMENT ON COLUMN tb_voos.num_aeronave IS 'Aeronave dos voos da cia.';


CREATE INDEX idx_origem
 ON tb_voos
 ( num_cidade_origem );

CREATE INDEX idx_destino
 ON tb_voos
 ( num_cidade_destino );

CREATE TABLE tb_voo_funcionario (
                num_funcionario NUMBER NOT NULL,
                num_voo NUMBER NOT NULL,
                CONSTRAINT PK_VOO_FUNCIONARIO PRIMARY KEY (num_funcionario, num_voo)
);


ALTER TABLE tb_voos ADD CONSTRAINT FK_AERONAVE_VOO
FOREIGN KEY (num_aeronave)
REFERENCES tb_aeronave (num_aeronave)
NOT DEFERRABLE;

ALTER TABLE tb_voos ADD CONSTRAINT FK_CIDADE_ORIGEM
FOREIGN KEY (num_cidade_origem)
REFERENCES tb_cidade (num_cidade)
NOT DEFERRABLE;

ALTER TABLE tb_voos ADD CONSTRAINT FK_CIDADE_DESTINO
FOREIGN KEY (num_cidade_destino)
REFERENCES tb_cidade (num_cidade)
NOT DEFERRABLE;

ALTER TABLE tb_voo_funcionario ADD CONSTRAINT FK_FUNCIONARIO_VOO
FOREIGN KEY (num_funcionario)
REFERENCES tb_funcionario (num_funcionario)
NOT DEFERRABLE;

ALTER TABLE tb_voo_funcionario ADD CONSTRAINT FK_VOO_FUNCIONARIO
FOREIGN KEY (num_voo)
REFERENCES tb_voos (num_voo)
NOT DEFERRABLE;
