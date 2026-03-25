-- 2,6)

CREATE TABLE funcionarios (
id INT PRIMARY KEY AUTO_INCREMENT,
nome VARCHAR(100) NOT NULL,
cargo VARCHAR(50) NOT NULL,
salario DECIMAL(10,2) NOT NULL,
departamentos_id INT,
FOREING KEY(departamentos_id)
REFERENCES departamentos(id));

INSERT INTO funcionarios(nome,cargo,salario) VALUES ("Pedro Lucas","Gerente",8000.00), ("Philips Henry Bartholomew","TI",6000..00)

-- 3)

ALTER TABLE funcionarios
ADD COLUMN data_admissao DATE NOT NULL;

INSERT INTO funcionarios(nome,cargo,salario,data_admissao) VALUES ("Pedro Lucas","Gerente",8000.00,"2020-07-16"), ("Philips Henry Bartholomew","TI",6000..00,"2022-08-22")

--4)

ALTER TABLE funcionarios
DROP COLUMN cargo;

INSERT INTO funcionarios(nome,salario,data_admissao) VALUES ("Pedro Lucas",8000.00,"2020-07-16"), ("Philips Henry Bartholomew",6000..00,"2022-08-22")

--5)

ALTER TABLE funcionarios
MODIFY COLUMN cargo DECIMAL(12,2);

INSERT INTO funcionarios(nome,salario,data_admissao) VALUES ("Pedro Lucas",8000.00,"2020-07-16"), ("Philips Henry Bartholomew",6000..00,"2022-08-22")

--6)

CREATE TABLE departementos (
id INT PRIMARY KEY AUTO INCREMENT, 
nome VARCHAR(100) NOT NULL);

INSERT INTO funcionarios(nome,salario,data_admissao,departamentos_id) VALUES ("Pedro Lucas",8000.00,"2020-07-16",2), ("Philips Henry Bartholomew",6000..00,"2022-08-22",1)

--7)

ALTER TABLE Setores
ADD COLUMN orcamentos: DECIMAL (12,2);

INSERT INTO Setores(nome,orcamentos) VALUES ("Publicidade", 5000.00), ("Vendas", 6500.00)

--8)

ALTER TABLE Setores
DROP COLUMN orcamentos;

INSERT INTO Setores(nome) VALUES ("Logistica"), ("Financeiro");

--9)

ALTER TABLE Setores
MODIFY COLUMN nome VARCHAR(150);

INSERT INTO Setores(nome) VALUES ("RH"), ("Produção");

--10)

ALTER TABLE departamentos
RENAME TO Setores;

INSERT INTO Setores(nome) VALUES ("Transporte"), ("Treinamentos");

--11)

DROP TABLE Setores;

--12)

ALTER TABLE Setores
ADD COLUMN Status VARCHAR (20) DEFAULT "Ativo";

 INSERT INTO funcionarios(nome, salario, data_admissao, status) VALUES ("André", 8500.00, "2017-04-15", "Ativo"), ("Zelda", 4000.00, "2024-05-02", "Inativo");