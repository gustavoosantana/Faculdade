-- 2,6
CREATE TABLE funcionarios (
id INT PRIMARY KEY AUTO_INCREMENT,
nome VARCHAR(100) NOT NULL,
cargo VARCHAR(50) NOT NULL,
salario DECIMAL(10,2) NOT NULL,
departamentos_id INT,
FOREING KEY(departamentos_id)
REFERENCES departamentos(id));

INSERT INTO funcionarios(nome,cargo,salario) VALUES ("Pedro Lucas","Gerente",8000.00), ("Philips Henry Bartholomew","TI",6000..00)

-- 3

ALTER TABLE funcionarios
ADD COLUMN data_admissao DATE NOT NULL;

INSERT INTO funcionarios(nome,cargo,salario,data_admissao) VALUES ("Pedro Lucas","Gerente",8000.00,"2020-07-16"), ("Philips Henry Bartholomew","TI",6000..00,"2022-08-22")

--4

ALTER TABLE funcionarios
DROP COLUMN cargo;

INSERT INTO funcionarios(nome,salario,data_admissao) VALUES ("Pedro Lucas",8000.00,"2020-07-16"), ("Philips Henry Bartholomew",6000..00,"2022-08-22")

--5

ALTER TABLE funcionarios
MODIFY COLUMN cargo DECIMAL(12,2);

CREATE TABLE departementos (
id INT PRIMARY KEY AUTO INCREMENT, 
nome VARCHAR(100) NOT NULL);

ALTER TABLE Setores
ADD COLUMN orcamentos: DECIMAL (12,2);

ALTER TABLE Setores
DROP COLUMN orcamentos;

ALTER TABLE Setores
MODIFY COLUMN nome VARCHAR(150);

ALTER TABLE departmentos
RENAME TO Setores;

DROP TABLE Setores;

ALTER TABLE Setores
ADD COLUMN Status VARCHAR (28) DEFAULT "Ativo";