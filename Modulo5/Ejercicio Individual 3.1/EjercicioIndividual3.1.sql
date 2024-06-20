CREATE DATABASE academia;
use academia;

-- Crear la tabla 'profesores'
CREATE TABLE profesores (
    id_profesor INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255),
    salario DECIMAL(10,2)
);

-- Crear la tabla 'cursos'
CREATE TABLE cursos (
    id_curso INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255),
    costo DECIMAL(10,2),
    duracion INT,
    id_profesor INT,
    FOREIGN KEY (id_profesor) REFERENCES profesores(id_profesor)
);

INSERT INTO profesores (nombre, salario) VALUES
('Juan Pérez', 3000),
('Ana Gómez', 3500),
('Luis Ramírez', 3200);

-- Insertar 3 profesores nuevos
INSERT INTO profesores (nombre, salario) VALUES
('Loreto Morales', 2000),
('Barbara Pardo', 1700),
('Carlos Lopez', 2300);

INSERT INTO cursos (nombre, costo, duracion, id_profesor) VALUES
('Curso de Vue', 200, 30, 1),
('Curso de JavaScript', 150, 45, 2),
('Curso de SQL', 100, 25, 3);

-- Insertar 3 cursos nuevos
INSERT INTO cursos (nombre, costo, duracion, id_profesor) VALUES
('Curso de Angular', 580, 45, 4),
('Curso de Python', 200, 70, 5),
('Curso de Java', 150, 25, 6);

-- Seleccionar el curso más costoso
SELECT * FROM cursos ORDER BY costo DESC LIMIT 1;

-- Seleccionar el profesor con el menor salario
SELECT * FROM profesores ORDER BY salario ASC LIMIT 1;

-- Seleccionar los cursos más costosos que el promedio
SELECT * FROM cursos WHERE costo > (SELECT AVG(costo) FROM cursos);

-- Crear la tabla Cursos económicos con los cursos menos costosos que el promedio
CREATE TABLE Cursos_economicos AS
SELECT * FROM cursos WHERE costo < (SELECT AVG(costo) FROM cursos);

-- Agregar campos a la tabla Cursos económicos
ALTER TABLE Cursos_economicos
ADD COLUMN `Cantidad mínima estudiantes` INT,
ADD COLUMN `Aportes públicos` DECIMAL(10,2),
ADD COLUMN `Costo realización` DECIMAL(10,2);

-- Renombrar la columna "Costo realización" a "Costo efectivo"
-- y restar el valor de 'Aportes públicos'
ALTER TABLE Cursos_economicos
CHANGE COLUMN `Costo realización` `Costo efectivo` DECIMAL(10,2);
UPDATE Cursos_economicos SET `Costo efectivo` = `Costo efectivo` - `Aportes públicos`;

-- Actualizar 5 cursos
UPDATE cursos SET
costo = costo + 50,
duracion = duracion + 5
WHERE id_curso IN (1, 2, 3, 4, 5);

-- Actualizar 3 profesores (asumiendo que los ID de los profesores son 1 a 3)
UPDATE profesores SET
salario = salario + 500
WHERE id_profesor IN (1, 2, 3);
