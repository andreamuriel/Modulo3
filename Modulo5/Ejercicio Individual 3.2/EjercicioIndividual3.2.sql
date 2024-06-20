CREATE DATABASE fenixstore;

-- Crear un usuario con todos los privilegios para la base de datos 'fenixstore'

CREATE USER 'tu_usuario'@'localhost' IDENTIFIED BY 'prueba01';
GRANT ALL PRIVILEGES ON fenixstore.* TO 'tu_usuario'@'localhost';
FLUSH PRIVILEGES;

USE fenixstore;

CREATE TABLE usuarios_inactivos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255),
    apellido VARCHAR(255),
    correo_electronico VARCHAR(255),
    telefono VARCHAR(20),
    genero ENUM('M', 'F', 'Otro')
);

CREATE TABLE usuarios_especiales (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255),
    apellido VARCHAR(255),
    correo_electronico VARCHAR(255),
    telefono VARCHAR(20),
    genero ENUM('M', 'F', 'Otro')
);

-- Insertar 5 usuarios en la tabla 'usuarios_inactivos'
INSERT INTO usuarios_inactivos (nombre, apellido, correo_electronico, telefono, genero) VALUES
('Andrea', 'Venegas', 'avenegas@gmail.com', '4564645747', 'F'),
('Sandra', 'Venegas', 'svenegas@gmail.com', '7465464666', 'F'),
('Eduardo', 'Venegas', 'evenegas@gmail.com', '4656454333', 'M'),
('Brandon', 'Choe', 'bchoe@gmail.com', '4678884564', 'M'),
('Elisabeth', 'Perez', 'eperez@gmail.com', '3244565466', 'F');

-- Transferir tres usuarios desde 'usuarios_inactivos' a 'usuarios_especiales'
INSERT INTO usuarios_especiales (nombre, apellido, correo_electronico, telefono, genero)
SELECT nombre, apellido, correo_electronico, telefono, genero FROM usuarios_inactivos WHERE id IN (1, 2, 3);

-- Anular la transferencia del tercer usuario)
DELETE FROM usuarios_especiales WHERE id = 3;
