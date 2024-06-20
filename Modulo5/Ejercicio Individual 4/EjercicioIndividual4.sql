-- Parte 1

-- Creacion BD y usuario

CREATE DATABASE fenixstore;
CREATE USER 'fenixadmin'@'localhost' IDENTIFIED BY 'prueba01';
GRANT ALL PRIVILEGES ON fenixstore.* TO 'fenixadmin'@'localhost';
USE fenixstore;

-- Parte 2

-- Tabla de usuarios

CREATE TABLE usuarios (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    contraseña VARCHAR(255),
    zona_horaria VARCHAR(5) DEFAULT 'UTC-3',
    genero ENUM('M', 'F'),
    telefono_contacto VARCHAR(20)
);

-- Tabla de ingresos

CREATE TABLE ingresos (
    id_ingreso INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT,
    fecha_hora_ingreso TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
);

-- Tabla de visitas

CREATE TABLE visitas (
    id_usuario INT,
    cantidad_visitas INT,
    PRIMARY KEY (id_usuario),
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
);

-- Parte 3

-- Insertar 8 registros por tabla

INSERT INTO usuarios (nombre, apellido, contraseña, genero, telefono_contacto) VALUES
('Camila', 'Beltran', 'ertgff', 'F', '7657776577'),
('Carolina', 'Sepulveda', '55ty.dd', 'F', '5566600987'),
('Sandra', 'Chavez', 'sdt5455', 'M', '657998433'),
('Nicolas', 'Nuñez', '3466dsvio', 'M', '223425555'),
('Manuel', 'Oñate', 'e4456ddd', 'M', '223455555'),
('Estefania', 'Pezo', 'qqwq44556', 'F', '399000076'),
('Diego', 'Aedo', 'ghhj.5566', 'M', '556678333'),
('Amanda', 'Velasquez', 'eerr-erwr.', 'F', '1113500985');

INSERT INTO ingresos (id_usuario, fecha_hora_ingreso) VALUES
(1, DEFAULT),
(2, DEFAULT),
(3, DEFAULT),
(4, DEFAULT),
(5, DEFAULT),
(6, DEFAULT),
(7, DEFAULT),
(8, DEFAULT);


INSERT INTO visitas (id_usuario, cantidad_visitas) VALUES
(1, 5),
(2, 2),
(3, 1),
(4, 8),
(5, 3),
(6, 7),
(7, 9),
(8, 2);

-- Parte 4: Eliminar una tabla

DROP TABLE visitas;


-- Justifique cada tipo de dato utilizado en la creación de las tablas.

-- INT para id_usuario e id_ingreso porque son numéricos
-- VARCHAR para nombre, apellido, contraseña y teléfono_contacto porque son cadenas de texto.
-- ENUM para género porque en mi definicion considere M y F.
-- TIMESTAMP para fecha_hora_ingreso para obtener hora de fecha actual con CURRENT_TIMESTAMP
-- INT para cantidad_visitas porque es numérico e ira aumentando en medida que se requiera.