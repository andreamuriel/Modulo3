CREATE DATABASE soporte;
USE soporte;

CREATE TABLE usuario (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    edad INT,
    correo_electronico VARCHAR(100),
    veces_usado INT DEFAULT 1
);

CREATE TABLE operario (
    id_operario INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    edad INT,
    correo_electronico VARCHAR(100),
    veces_soporte INT DEFAULT 1
);

CREATE TABLE soporte (
    id_soporte INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT,
    id_operario INT,
    fecha DATE,
    evaluación INT,
    comentario TEXT,
    FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario),
    FOREIGN KEY (id_operario) REFERENCES operario(id_operario)
);

-- Insertar 5 usuarios
INSERT INTO usuario (nombre, apellido, edad, correo_electronico, veces_usado) VALUES
('Andrea', 'Venegas', 26, 'andvenegas@gmail.com', 1),
('Sandra', 'Venegas', 59, 's.venegas@gmail.com', 2),
('Eric', 'Venegas', 25, 'evenegas@gmail.com', 3),
('Tim', 'Choe', 18, 'tchoe@gmail.com', 4),
('Brandon', 'Choe', 30, 'bchoe@gmail.com', 5);

-- Insertar 5 operadores
INSERT INTO operario (nombre, apellido, edad, correo_electronico, veces_soporte) VALUES
('Nicolas', 'Diaz', 30, 'ndiaz@fenixstore.com', 1),
('Bastian', 'SanMartin', 26, 'bast.sanmartin@fenixstore.com', 2),
('Camila', 'Beltran', 27, 'cabeltran@fenixstore.com', 3),
('Benjamin', 'Fuentealba', 27, 'bfuentealba@fenixstore.com', 4),
('Cristian', 'Cid', 28, 'ccid@fenixstore.com', 5);

-- Insertar 10 operaciones de soporte
INSERT INTO soporte (id_usuario, id_operario, fecha, evaluación, comentario) VALUES
(1, 1, '2024-03-21', 5, 'Buen servicio'),
(2, 2, '2024-01-24', 6, 'Excelente atención'),
(3, 3, '2024-02-16', 4, 'Respuesta rápida'),
(4, 4, '2024-01-01', 7, 'Muy amable y eficiente'),
(5, 5, '2024-03-09', 3, 'Podría mejorar'),
(1, 2, '2024-02-23', 2, 'No resolvió mi problema'),
(2, 3, '2024-01-19', 7, 'Perfecto, gracias'),
(3, 4, '2024-04-15', 6, 'Muy satisfecho'),
(4, 5, '2024-03-12', 1, 'Mal servicio'),
(5, 1, '2024-02-10', 5, 'Ayuda adecuada');

-- Seleccionar las 3 operaciones con mejor evaluación
SELECT * FROM soporte ORDER BY evaluación DESC LIMIT 3;

-- Seleccionar las 3 operaciones con menos evaluación
SELECT * FROM soporte ORDER BY evaluación LIMIT 3;

-- Seleccionar al operario que más soportes ha realizado
SELECT id_operario, COUNT(*) as numero_soportes FROM soporte GROUP BY id_operario ORDER BY numero_soportes DESC LIMIT 1;

-- Seleccionar al cliente que menos veces ha utilizado la aplicación
SELECT id_usuario FROM usuario ORDER BY veces_usado LIMIT 1;

-- Agregar 10 años a los tres primeros usuarios registrados
UPDATE Usuario SET edad = edad + 10 ORDER BY id_usuario LIMIT 3;

-- Renombrar todas las columnas ‘correo electrónico’
ALTER TABLE usuario CHANGE correo_electronico email VARCHAR(100);
ALTER TABLE operario CHANGE correo_electronico email VARCHAR(100);

-- Seleccionar solo los operarios mayores de 20 años
SELECT * FROM operario WHERE edad > 20;
