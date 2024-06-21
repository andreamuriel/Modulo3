CREATE DATABASE DbTelovendo;

CREATE USER 'adminTelovendo'@'localhost' IDENTIFIED BY 'telovendo123';
GRANT ALL PRIVILEGES ON DbTelovendo.* TO 'adminTelovendo'@'localhost';

USE DbTelovendo;

CREATE TABLE Usuarios (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY, -- Se usa para genera de forma unica y autoincremental numeros
    nombre VARCHAR(50) NOT NULL, -- Se usa VARCHAR para guardar nombres de longitud variable
    apellido VARCHAR(50) NOT NULL, -- Se usa VARCHAR para guardar apellidos de longitud variable
    contrasena VARCHAR(255) NOT NULL, -- Se usa VARCHAR para la contraseña para permitir contreñas encriptadas de longitud variable
    zona_horaria VARCHAR(6) DEFAULT 'UTC-3', -- VARCHAR para guardar zonas horarias como texto
    genero ENUM('M', 'F', 'Otro') NOT NULL, -- ENUM es lo mejor para valores predefinidos y limitados
    telefono_contacto VARCHAR(20) NOT NULL -- VARCHAR es lo mejor para diferentes formatos de números telefónicos
);

CREATE TABLE Ingresos (
    id_ingreso INT AUTO_INCREMENT PRIMARY KEY, -- Se usa para genera de forma unica y autoincremental numeros
    id_usuario INT NOT NULL, -- Se usa INT ya que se requieren numeros
    fecha_hora_ingreso TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- TIMESTAMP para registrar la fecha y hora exacta del ingreso
    FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario)
);

CREATE TABLE Contactos (
    id_contacto INT AUTO_INCREMENT PRIMARY KEY, -- Se usa para genera de forma unica y autoincremental numeros
    id_usuario INT NOT NULL, -- Se usa INT ya que se requieren numeros
    numero_telefono VARCHAR(20) NOT NULL UNIQUE, -- VARCHAR es lo mejor para diferentes formatos de números telefónicos
    correo_electronico VARCHAR(100) NOT NULL, -- VARCHAR es adecuado para correos electrónicos
    FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario)
);

-- Modificar la zona horaria por defecto a UTC-2
ALTER TABLE Usuarios ALTER zona_horaria SET DEFAULT 'UTC-2';

-- Insertar 8 registros por tabla

INSERT INTO Usuarios (nombre, apellido, contrasena, genero, telefono_contacto) VALUES
('Antonio', 'Romero', 'fgdherther', 'M', '+5691325558'),
('Alejandra', 'Pizarro', 'retougoeurg', 'F', '+569835677721'),
('Constanza', 'Irribarra', 'ergergregevv', 'F', '+56916433344'),
('Marta', 'Pérez', 'vvbevrieiee', 'F', '+569422224411'),
('Loreto', 'Torres', 'eriutrywerywe', 'F', '+56932355588'),
('Martin', 'Manrriquez', 'werwerwerwercc', 'M', '+56912212355'),
('Camila', 'Flores', 'weorupqbcfwef', 'F', '+56444677766'),
('Kevin', 'Paz', 'weroweprweuryyy', 'M', '+5694221145544');

INSERT INTO Ingresos (id_usuario, fecha_hora_ingreso) VALUES
(1, '2024-02-21 18:43:28'),
(2, '2024-04-14 19:09:00'),
(3, '2024-03-23 09:15:30'),
(4, '2024-01-01 11:05:42'),
(5, '2024-02-05 11:20:55'),
(6, '2024-04-07 18:45:33'),
(7, '2024-03-13 21:30:29'),
(8, '2024-02-19 16:00:00');

INSERT INTO Contactos (id_usuario, numero_telefono, correo_electronico) VALUES
(1, '+5691325558', 'aromero@gmail.com'),
(2, '+569835677721', 'apizarro@gmail.com'),
(3, '+56916433344', 'cirribarra@gmail.com'),
(4, '+569422224411', 'mperez@gmail.com'),
(5, '+56932355588', 'ltorres@gmail.com'),
(6, '+56912212355', 'mmanrriquez@gmail.com'),
(7, '+56444677766', 'cflores@gmail.com'),
(8, '+5694221145544', 'kpaz@gmail.com');

-- Modifique la columna teléfono de contacto, para crear un vínculo entre la tabla Usuarios y la tabla Contactos.
ALTER TABLE Usuarios ADD CONSTRAINT fk_contacto FOREIGN KEY (telefono_contacto) REFERENCES Contactos(numero_telefono);


