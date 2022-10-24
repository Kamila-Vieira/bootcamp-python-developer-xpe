
CREATE TABLE colaboradores (
                colaborador_id INT NOT NULL,
                matricula VARCHAR NOT NULL,
                nome VARCHAR NOT NULL,
                email VARCHAR NOT NULL,
                CONSTRAINT pk_colaboradores PRIMARY KEY (colaborador_id)
)
CREATE UNIQUE  NONCLUSTERED INDEX colaboradores_idx
 ON colaboradores
 ( matricula )


CREATE TABLE componentes (
                componente_id INT NOT NULL,
                nome VARCHAR NOT NULL,
                categoria VARCHAR NOT NULL,
                colaborador_id INT NOT NULL,
                CONSTRAINT pk_componente PRIMARY KEY (componente_id)
)

CREATE TABLE tarefas (
                tarefa_id INT NOT NULL,
                tipo VARCHAR NOT NULL,
                nome VARCHAR NOT NULL,
                componente_id INT NOT NULL,
                colaborador_id INT NOT NULL,
                CONSTRAINT pk_tarefa PRIMARY KEY (tarefa_id)
)

CREATE TABLE documentos (
                documento_id INT NOT NULL,
                titulo VARCHAR NOT NULL,
                descricao VARCHAR NOT NULL,
                tarefa_id INT NOT NULL,
                CONSTRAINT pk_documento PRIMARY KEY (documento_id)
)

CREATE TABLE areas (
                area_id INT NOT NULL,
                nome VARCHAR NOT NULL,
                CONSTRAINT pk_area PRIMARY KEY (area_id)
)

CREATE TABLE projetos (
                projetos_id INT NOT NULL,
                nome VARCHAR NOT NULL,
                data_inicio VARCHAR NOT NULL,
                area_id INT NOT NULL,
                documento_id INT NOT NULL,
                colaborador_id INT NOT NULL,
                CONSTRAINT pk_projetos PRIMARY KEY (projetos_id)
)

ALTER TABLE projetos ADD CONSTRAINT colaboradores_projetos_fk
FOREIGN KEY (colaborador_id)
REFERENCES colaboradores (colaborador_id)
ON DELETE NO ACTION
ON UPDATE NO ACTION

ALTER TABLE tarefas ADD CONSTRAINT colaboradores_tarefas_fk
FOREIGN KEY (colaborador_id)
REFERENCES colaboradores (colaborador_id)
ON DELETE NO ACTION
ON UPDATE NO ACTION

ALTER TABLE componentes ADD CONSTRAINT colaboradores_componentes_fk
FOREIGN KEY (colaborador_id)
REFERENCES colaboradores (colaborador_id)
ON DELETE NO ACTION
ON UPDATE NO ACTION

ALTER TABLE tarefas ADD CONSTRAINT componentes_tarefas_fk
FOREIGN KEY (componente_id)
REFERENCES componentes (componente_id)
ON DELETE NO ACTION
ON UPDATE NO ACTION

ALTER TABLE documentos ADD CONSTRAINT tarefas_documentos_fk
FOREIGN KEY (tarefa_id)
REFERENCES tarefas (tarefa_id)
ON DELETE NO ACTION
ON UPDATE NO ACTION

ALTER TABLE projetos ADD CONSTRAINT documentos_projetos_fk
FOREIGN KEY (documento_id)
REFERENCES documentos (documento_id)
ON DELETE NO ACTION
ON UPDATE NO ACTION

ALTER TABLE projetos ADD CONSTRAINT areas_projetos_fk
FOREIGN KEY (area_id)
REFERENCES areas (area_id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
