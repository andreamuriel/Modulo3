CREATE DATABASE telovendo;
CREATE USER 'admintienda'@'localhost' IDENTIFIED BY 'admin123';
GRANT ALL PRIVILEGES ON telovendo.* TO 'admintienda'@'localhost';
FLUSH PRIVILEGES;
SHOW DATABASES;

USE telovendo;
CREATE TABLE cliente (
    ClienteID INT AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(50),
    Apellido VARCHAR(50),
    Teléfono VARCHAR(50),
    Dirección VARCHAR(50),
    Comuna VARCHAR(50),
    Correo VARCHAR(50),
    Registro VARCHAR(50)
);

CREATE TABLE producto (
    ProductoID INT AUTO_INCREMENT PRIMARY KEY,
    SKU VARCHAR(50),
    Categoría VARCHAR(50),
    Productor VARCHAR(50),
    Stock VARCHAR(100)
);

CREATE TABLE vendedor (
    VendedorID INT AUTO_INCREMENT PRIMARY KEY,
    RUN VARCHAR(50),
    Nombre VARCHAR(50),
    Apellido VARCHAR(50),
    Nacimiento VARCHAR(50),
    Sección VARCHAR(50)
);

DESCRIBE cliente;
INSERT INTO cliente(Nombre, Apellido, Teléfono, Dirección, Comuna, Correo, Registro) VALUES ('Nicolas', 'Diaz', '944431048', 'Av. San Martín 1030', 'Mejillones', 'nicolas.diaz@cuidadoverde.com', '06/03/2024');
INSERT INTO cliente(Nombre, Apellido, Teléfono, Dirección, Comuna, Correo, Registro) VALUES ('Ignacio', 'Armijo', '944431333', 'Av. San Martín 1030', 'Mejillones', 'iarmijo@cuidadoverde.com', '06/04/2024'), ('Sebastian', 'Moreira', '944431448', 'Av. San Martín 1030', 'Santiago', 's.moreira@cuidadoverde.com', '06/03/2024'), ('Matias', 'Ramirez', '944444048', 'Av. San José 1050', 'Santiago', 'matias.Ramirez@gmail.com', '02/05/2023'), ('Camila', 'Beltran', '948889322', 'Av. General Mackena 1030', 'Santiago', 'Camila.Beltran@gmail.com', '02/05/2023'), ('Ivan', 'Coyhaique', '944434097', 'Av. Almirante Latorre 230', 'Santiago', 'Ivan.Coyhaique@gmail.com', '02/05/2023'), ('Patricio', 'Vega', '900000988', 'Av. Bellavsiat 185', 'Santiago', 'Patricio.Vega@gmail.com', '02/05/2023');
SELECT * FROM cliente;
INSERT INTO cliente(Nombre, Apellido, Teléfono, Dirección, Comuna, Correo, Registro) VALUES ('Johana', 'Cid', '944441744', 'Av. Algarrobo 1321', 'Pta Arenas', 'jocid@gmail.com', '05/07/2023');
INSERT INTO cliente(Nombre, Apellido, Teléfono, Dirección, Comuna, Correo, Registro) VALUES ('Daniela', 'Bernales', '978577383', 'Calle Cisterna 564', 'Arica', 'danielabernales@gmail.com', '09/01/2023');
INSERT INTO cliente(Nombre, Apellido, Teléfono, Dirección, Comuna, Correo, Registro) VALUES ('Matias', 'Muñoz', '98379883', 'Pasaje Olivar 345', 'Iquique', 'Mmunoz@gmail.com', '06/02/2023');
INSERT INTO cliente(Nombre, Apellido, Teléfono, Dirección, Comuna, Correo, Registro) VALUES ('Tomás', 'Barros', '98473802', 'Pasaje Olivar 345', 'Calama', 'Tomas@gmail.com', '06/02/2023');
INSERT INTO cliente(Nombre, Apellido, Teléfono, Dirección, Comuna, Correo, Registro) VALUES ('Eduardo', 'Muñoz', '989895278', 'Pasaje Bellavista 754', 'Iquique', 'Pablo@gmail.com', '02/07/2023');
INSERT INTO cliente(Nombre, Apellido, Teléfono, Dirección, Comuna, Correo, Registro) VALUES ('José', 'Venegas', '983793453', 'Pasaje Olivar 345', 'Antofagasta', 'jose@gmail.com', '09/02/2023');
INSERT INTO cliente(Nombre, Apellido, Teléfono, Dirección, Comuna, Correo, Registro) VALUES ('Matias', 'Morales', '98379883', 'Calle Colombia 1030', 'Antofagasta', 'matm@gmail.com', '13/06/2023');
INSERT INTO cliente(Nombre, Apellido, Teléfono, Dirección, Comuna, Correo, Registro) VALUES ('Amanda', 'Velasquez', '967343921', 'Calle Almirante Latorre 345', 'Mejillones', 'Amand@gmail.com', '06/02/2023');

DESCRIBE producto;
INSERT INTO producto(SKU, Categoría, Productor, Stock) VALUES ('01', 'Mouse', 'Nvida', 20);
INSERT INTO producto(SKU, Categoría, Productor, Stock) VALUES ('02', 'Pantalla', 'LG', 40);
INSERT INTO producto(SKU, Categoría, Productor, Stock) VALUES ('03', 'Teclado', 'Nvida', 30);
INSERT INTO producto(SKU, Categoría, Productor, Stock) VALUES ('04', 'Audifonos', 'Logitech', 10);
INSERT INTO producto(SKU, Categoría, Productor, Stock) VALUES ('05', 'Cable HDMI', 'LG', 20);
INSERT INTO producto(SKU, Categoría, Productor, Stock) VALUES ('06', 'Celular', 'Sony', 20);
INSERT INTO producto(SKU, Categoría, Productor, Stock) VALUES ('07', 'SillaGamer', 'Lider', 40);
INSERT INTO producto(SKU, Categoría, Productor, Stock) VALUES ('08', 'Escritorio', 'Lider', 20);
INSERT INTO producto(SKU, Categoría, Productor, Stock) VALUES ('09', 'MousePro', 'Nvida', 10);
INSERT INTO producto(SKU, Categoría, Productor, Stock) VALUES ('10', 'PantallaWide', 'LG', 10);

SELECT * FROM producto;
DELETE FROM vendedor where VendedorID = 1;

DESCRIBE vendedor;
INSERT INTO vendedor(RUN, Nombre, Apellido, Nacimiento, Sección) VALUES ('19445833-9', 'Vladimir', 'Esparza', '06/03/97', 'Ofimatica');
INSERT INTO vendedor(RUN, Nombre, Apellido, Nacimiento, Sección) VALUES ('12345679-9', 'Jaime', 'Rohten', '03/05/97', 'Ofimatica');
INSERT INTO vendedor(RUN, Nombre, Apellido, Nacimiento, Sección) VALUES ('13782334-7', 'Cristian', 'Aguilera', '02/05/98', 'Ofimatica');
INSERT INTO vendedor(RUN, Nombre, Apellido, Nacimiento, Sección) VALUES ('20388923-9', 'Luis', 'Duran', '02/03/99', 'Gamer');
INSERT INTO vendedor(RUN, Nombre, Apellido, Nacimiento, Sección) VALUES ('23489173-4', 'Ernesto', 'Rubio', '08/04/00', 'Gamer');
INSERT INTO vendedor(RUN, Nombre, Apellido, Nacimiento, Sección) VALUES ('22994792-K', 'Juan', 'Antipil', '10/02/95', 'Gamer');
INSERT INTO vendedor(RUN, Nombre, Apellido, Nacimiento, Sección) VALUES ('18374892-2', 'Natalia', 'Risso', '06/04/97', 'Atención Cliente');
INSERT INTO vendedor(RUN, Nombre, Apellido, Nacimiento, Sección) VALUES ('13489302-9', 'Juan', 'Saez', '02/10/96', 'Atención Cliente');
INSERT INTO vendedor(RUN, Nombre, Apellido, Nacimiento, Sección) VALUES ('12893093-8', 'Felipe', 'Oñate', '05/02/99', 'Atención Cliente');
INSERT INTO vendedor(RUN, Nombre, Apellido, Nacimiento, Sección) VALUES ('20389402-7', 'Brian', 'Hermosilla', '03/03/95', 'Atención Cliente');

SELECT * FROM vendedor;

-- ALTER TABLE
ALTER TABLE producto ADD Precio DECIMAL(10,2);
ALTER TABLE vendedor ADD Salario INT;
ALTER TABLE cliente ADD TotalPagado DECIMAL(10,2);
SELECT * FROM producto;
SELECT * FROM vendedor;
SELECT * FROM cliente;


-- UPDATE
UPDATE `telovendo`.`producto` SET `Precio` = '20' WHERE (`ProductoID` = '2');
UPDATE `telovendo`.`producto` SET `Precio` = '30' WHERE (`ProductoID` = '3');
UPDATE `telovendo`.`producto` SET `Precio` = '12' WHERE (`ProductoID` = '4');
UPDATE `telovendo`.`producto` SET `Precio` = '16' WHERE (`ProductoID` = '5');
UPDATE `telovendo`.`producto` SET `Precio` = '5' WHERE (`ProductoID` = '6');
UPDATE `telovendo`.`producto` SET `Precio` = '50' WHERE (`ProductoID` = '7');
UPDATE `telovendo`.`producto` SET `Precio` = '60' WHERE (`ProductoID` = '8');
UPDATE `telovendo`.`producto` SET `Precio` = '100' WHERE (`ProductoID` = '9');
UPDATE `telovendo`.`producto` SET `Precio` = '45' WHERE (`ProductoID` = '10');
UPDATE `telovendo`.`producto` SET `Precio` = '150' WHERE (`ProductoID` = '11');

UPDATE `telovendo`.`vendedor` SET `Salario` = '1000' WHERE (`VendedorID` = '2');
UPDATE `telovendo`.`vendedor` SET `Salario` = '1000' WHERE (`VendedorID` = '3');
UPDATE `telovendo`.`vendedor` SET `Salario` = '2000' WHERE (`VendedorID` = '4');
UPDATE `telovendo`.`vendedor` SET `Salario` = '2500' WHERE (`VendedorID` = '5');
UPDATE `telovendo`.`vendedor` SET `Salario` = '950' WHERE (`VendedorID` = '6');
UPDATE `telovendo`.`vendedor` SET `Salario` = '800' WHERE (`VendedorID` = '7');
UPDATE `telovendo`.`vendedor` SET `Salario` = '1500' WHERE (`VendedorID` = '8');
UPDATE `telovendo`.`vendedor` SET `Salario` = '2800' WHERE (`VendedorID` = '9');
UPDATE `telovendo`.`vendedor` SET `Salario` = '2500' WHERE (`VendedorID` = '10');
UPDATE `telovendo`.`vendedor` SET `Salario` = '1900' WHERE (`VendedorID` = '11');
UPDATE `telovendo`.`vendedor` SET `Salario` = '1500' WHERE (`VendedorID` = '12');

UPDATE `telovendo`.`cliente` SET `TotalPagado` = '500' WHERE (`ClienteID` = '1');
UPDATE `telovendo`.`cliente` SET `TotalPagado` = '600' WHERE (`ClienteID` = '2');
UPDATE `telovendo`.`cliente` SET `TotalPagado` = '2000' WHERE (`ClienteID` = '3');
UPDATE `telovendo`.`cliente` SET `TotalPagado` = '850' WHERE (`ClienteID` = '4');
UPDATE `telovendo`.`cliente` SET `TotalPagado` = '650' WHERE (`ClienteID` = '5');
UPDATE `telovendo`.`cliente` SET `TotalPagado` = '1000' WHERE (`ClienteID` = '6');
UPDATE `telovendo`.`cliente` SET `TotalPagado` = '400' WHERE (`ClienteID` = '7');
UPDATE `telovendo`.`cliente` SET `TotalPagado` = '350' WHERE (`ClienteID` = '8');
UPDATE `telovendo`.`cliente` SET `TotalPagado` = '200' WHERE (`ClienteID` = '9');
UPDATE `telovendo`.`cliente` SET `TotalPagado` = '2500' WHERE (`ClienteID` = '10');
UPDATE `telovendo`.`cliente` SET `TotalPagado` = '450' WHERE (`ClienteID` = '11');
UPDATE `telovendo`.`cliente` SET `TotalPagado` = '500' WHERE (`ClienteID` = '12');
UPDATE `telovendo`.`cliente` SET `TotalPagado` = '780' WHERE (`ClienteID` = '13');
UPDATE `telovendo`.`cliente` SET `TotalPagado` = '800' WHERE (`ClienteID` = '14');
UPDATE `telovendo`.`cliente` SET `TotalPagado` = '250' WHERE (`ClienteID` = '15');

-- Análisis
-- Seleccione los vendedores que tienen un salario superior al promedio.
SELECT AVG(Salario) AS PromedioSalario FROM vendedor;
SELECT * from vendedor WHERE Salario > (SELECT AVG(Salario) AS PromedioSalario FROM vendedor);
-- Seleccione los productos más caros que el promedio.
SELECT AVG(Precio) AS PromedioPrecio From producto;
SELECT * FROM producto WHERE Precio > (SELECT AVG(Precio) AS PromedioPrecio From producto);
-- Seleccione los clientes que han pagado más que el promedio.
SELECT AVG(TotalPagado) AS PromedioTotalPagado From cliente;
SELECT * FROM cliente WHERE TotalPagado > (SELECT AVG(TotalPagado) AS PromedioTotalPagado From cliente);
-- Indique cuántos vendedores tienen un salario inferior al promedio.
SELECT * from vendedor WHERE Salario < (SELECT AVG(Salario) AS PromedioSalario FROM vendedor);
-- Indique cuántos productos son más baratos que el promedio.
SELECT * FROM producto WHERE Precio < (SELECT AVG(Precio) AS PromedioPrecio From producto);
-- Seleccione el nombre y el apellido de los vendedores que tienen un salario superior al promedio.
SELECT Nombre, Apellido FROM vendedor WHERE Salario > (SELECT AVG(Salario) AS PromedioSalario FROM vendedor);
-- Indique cuál es el producto más barato y el producto más caro del inventario.
SELECT Categoría, Precio from producto WHERE Precio = (SELECT MIN(Precio) AS PrecioMinimo FROM producto);
SELECT Categoría, Precio from producto WHERE Precio = (SELECT MAX(Precio) AS PrecioMinimo FROM producto);
-- Indique cual es el costo de comprar uno de cada producto en el inventario.
SELECT SUM(Precio) AS CostoTotal FROM producto;
-- Identifique la comuna que tiene más clientes registrados.
SELECT Comuna, COUNT(*) AS ComunaClientes FROM cliente GROUP BY Comuna ORDER BY ComunaClientes DESC LIMIT 1;
-- Identifique los productos que tienen más de 5 unidades en stock.
SELECT Categoría, Stock FROM producto WHERE Stock > 5;

-- Qué utilidad tiene el campo AUTO INCREMENT al definir una columna de atributo. ¿En qué casos crees que es útil?
-- El campo AUTO INCREMENT asigna automáticamente un número único a una columna cada vez que se inserta un nuevo registro. Es útil para generar identificadores únicos automáticamente, simplificando la gestión de datos y asegurando la integridad de la base de datos.