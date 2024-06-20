
-- CREAR BD

CREATE DATABASE IF NOT EXISTS fenix_store;

-- USAR BD

USE fenix_store;

-- CREAR TABLAS

CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    contrasena VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS pedidos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NOT NULL,
    producto VARCHAR(255) NOT NULL,
    cantidad INT NOT NULL,
    fecha_pedido TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);

-- INSERTAR DATOS

INSERT INTO usuarios (nombre, email, contrasena)
VALUES ('Andres Lopez', 'andres@gmail.com', '123456');

INSERT INTO usuarios (nombre, email, contrasena)
VALUES ('Fernando García', 'fernando@gmail.com', '56789');

INSERT INTO usuarios (nombre, email, contrasena)
VALUES ('María López', 'maria@gmail.com', '89012');

INSERT INTO pedidos (usuario_id, producto, cantidad)
VALUES (1, 'PS5', 1);

INSERT INTO pedidos (producto, cantidad, usuario_id)
VALUES ('XBOX', 2, 1);

INSERT INTO pedidos (producto, cantidad, usuario_id)
VALUES ('Nintendo Switch', 3, 2);

-- CONSULTAS

SELECT p.id, p.producto, p.cantidad, p.fecha_pedido
FROM pedidos p
JOIN usuarios u ON p.usuario_id = u.id
WHERE u.nombre = 'Andres Lopez';


SELECT producto, SUM(cantidad) AS total_vendido
FROM pedidos
GROUP BY producto
ORDER BY total_vendido DESC
LIMIT 5;

UPDATE usuarios
SET email = 'andres_new_email@gmail.com'
WHERE id = 1;

DELETE FROM pedidos
WHERE fecha_pedido < '2024-04-08';

SELECT AVG(cantidad) AS promedio_cantidad
FROM pedidos;