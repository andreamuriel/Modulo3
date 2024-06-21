-- Identifique cual es el salario mínimo entre vendedores.
SELECT MIN(Salario) as SalarioMinimo FROM vendedor;
SELECT Nombre, Salario as SalarioMinimo FROM vendedor where Salario = (SELECT  MIN(Salario) FROM vendedor);
-- Identifique cual es el salario máximo entre vendedores.
SELECT Nombre, Salario as SalarioMaximo FROM vendedor where Salario = (SELECT  MAX(Salario) FROM vendedor);
-- Súmele el salario mínimo identificado al salario de todos los vendedores.
SELECT Nombre, Salario + (SELECT MIN(Salario) FROM vendedor) AS SalarioTotal from vendedor;
-- Elimine el producto más caro del inventario.
SELECT MAX(Precio) as PrecioMax from producto;
SELECT Categoría, Precio AS PrecioMax FROM producto WHERE Precio = (SELECT MAX(Precio) FROM producto);
DELETE FROM producto WHERE Precio = (SELECT MAX(Precio) FROM producto);
-- Cree una tabla que contenga solo los clientes que han pagado más que el promedio.
SELECT * FROM cliente;
SELECT AVG(TotalPagado) FROM cliente;
CREATE TABLE clientes_VIP AS SELECT * FROM cliente WHERE TotalPagado > (SELECT AVG(TotalPagado) FROM cliente);
SELECT * FROM clientes_VIP;
-- Actualice los datos de tres productos.
SELECT * FROM producto;
UPDATE producto SET precio = 40 WHERE productoID IN (2, 3, 4);
-- Actualice los datos de tres vendedores.
SELECT * from vendedor;
UPDATE vendedor SET Salario = 1000 WHERE VendedorID IN (3, 4, 5);
-- Actualice los datos de 1 cliente.
SELECT * from cliente;
UPDATE cliente SET TotalPagado = 1000 WHERE clienteID = 1;
-- Seleccione el nombre y el apellido de los vendedores que tienen un salario superior al promedio.
SELECT nombre, apellido FROM vendedor WHERE Salario > (SELECT AVG(Salario) FROM vendedor);
-- Indique cuál es el cliente con mayor gasto.
SELECT Nombre, apellido FROM cliente WHERE totalpagado = (SELECT MAX(totalpagado) FROM cliente);

-- ACTUALIZACIÓN DE TABLAS

INSERT INTO vendedor(RUN, Nombre, Apellido, Nacimiento, Sección) VALUES ('19445833-9', 'Vladimir', 'Esparza', '06/03/97', 'Ofimatica');
INSERT INTO vendedor(RUN, Nombre, Apellido, Nacimiento, Sección) VALUES ('12345679-9', 'Jaime', 'Rohten', '03/05/97', 'Ofimatica');
INSERT INTO vendedor(RUN, Nombre, Apellido, Nacimiento, Sección) VALUES ('13782334-7', 'Cristian', 'Aguilera', '02/05/98', 'Ofimatica');
INSERT INTO vendedor(RUN, Nombre, Apellido, Nacimiento, Sección) VALUES ('20388923-9', 'Luis', 'Duran', '02/03/99', 'Gamer');
INSERT INTO vendedor(RUN, Nombre, Apellido, Nacimiento, Sección) VALUES ('23489173-4', 'Ernesto', 'Rubio', '08/04/00', 'Gamer');

INSERT INTO producto(SKU, Categoría, Productor, Stock) VALUES ('01', 'Mouse', 'Nvida', 20);
INSERT INTO producto(SKU, Categoría, Productor, Stock) VALUES ('02', 'Pantalla', 'LG', 40);
INSERT INTO producto(SKU, Categoría, Productor, Stock) VALUES ('03', 'Teclado', 'Nvida', 30);
INSERT INTO producto(SKU, Categoría, Productor, Stock) VALUES ('04', 'Audifonos', 'Logitech', 10);
INSERT INTO producto(SKU, Categoría, Productor, Stock) VALUES ('05', 'Cable HDMI', 'LG', 20);


INSERT INTO cliente(Nombre, Apellido, Teléfono, Dirección, Comuna, Correo, Registro) VALUES ('Tomás', 'Barros', '98473802', 'Pasaje Olivar 345', 'Calama', 'Tomas@gmail.com', '06/02/2023');
INSERT INTO cliente(Nombre, Apellido, Teléfono, Dirección, Comuna, Correo, Registro) VALUES ('Eduardo', 'Muñoz', '989895278', 'Pasaje Bellavista 754', 'Iquique', 'Pablo@gmail.com', '02/07/2023');
INSERT INTO cliente(Nombre, Apellido, Teléfono, Dirección, Comuna, Correo, Registro) VALUES ('José', 'Venegas', '983793453', 'Pasaje Olivar 345', 'Antofagasta', 'jose@gmail.com', '09/02/2023');
INSERT INTO cliente(Nombre, Apellido, Teléfono, Dirección, Comuna, Correo, Registro) VALUES ('Matias', 'Morales', '98379883', 'Calle Colombia 1030', 'Antofagasta', 'matm@gmail.com', '13/06/2023');
INSERT INTO cliente(Nombre, Apellido, Teléfono, Dirección, Comuna, Correo, Registro) VALUES ('Amanda', 'Velasquez', '967343921', 'Calle Almirante Latorre 345', 'Mejillones', 'Amand@gmail.com', '06/02/2023');




