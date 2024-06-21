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

INSERT INTO cliente(Nombre, Apellido, Teléfono, Dirección, Comuna, Correo, Registro) VALUES ('Nicolas', 'Diaz', '944431048', 'Av. San Martín 1030', 'Mejillones', 'nicolas.diaz@cuidadoverde.com', '06/03/2024');
INSERT INTO cliente(Nombre, Apellido, Teléfono, Dirección, Comuna, Correo, Registro) VALUES ('Ignacio', 'Armijo', '944431333', 'Av. San Martín 1030', 'Mejillones', 'iarmijo@cuidadoverde.com', '06/04/2024'), ('Sebastian', 'Moreira', '944431448', 'Av. San Martín 1030', 'Santiago', 's.moreira@cuidadoverde.com', '06/03/2024'), ('Matias', 'Ramirez', '944444048', 'Av. San José 1050', 'Santiago', 'matias.Ramirez@gmail.com', '02/05/2023'), ('Camila', 'Beltran', '948889322', 'Av. General Mackena 1030', 'Santiago', 'Camila.Beltran@gmail.com', '02/05/2023'), ('Ivan', 'Coyhaique', '944434097', 'Av. Almirante Latorre 230', 'Santiago', 'Ivan.Coyhaique@gmail.com', '02/05/2023'), ('Patricio', 'Vega', '900000988', 'Av. Bellavsiat 185', 'Santiago', 'Patricio.Vega@gmail.com', '02/05/2023');
SELECT * FROM cliente;
INSERT INTO cliente(Nombre, Apellido, Teléfono, Dirección, Comuna, Correo, Registro) VALUES ('Johana', 'Cid', '944441744', 'Av. Algarrobo 1321', 'Pta Arenas', 'jocid@gmail.com', '05/07/2023');
INSERT INTO cliente(Nombre, Apellido, Teléfono, Dirección, Comuna, Correo, Registro) VALUES ('Daniela', 'Bernales', '978577383', 'Calle Cisterna 564', 'Arica', 'danielabernales@gmail.com', '09/01/2023');
INSERT INTO cliente(Nombre, Apellido, Teléfono, Dirección, Comuna, Correo, Registro) VALUES ('Matias', 'Muñoz', '98379883', 'Pasaje Olivar 345', 'Iquique', 'Mmunoz@gmail.com', '06/02/2023');

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

Describe vendedor;
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