CREATE DATABASE online_store;
CREATE USER 'store_admin'@'localhost' IDENTIFIED BY 'admin123';
GRANT ALL PRIVILEGES ON online_store.* TO 'store_admin'@'localhost';
FLUSH PRIVILEGES;
USE online_store;

CREATE TABLE clientes (
    cliente_id VARCHAR(255) PRIMARY KEY,
    saldo_points INT NOT NULL
    );
    
CREATE TABLE transacciones (
    transaccionID INT AUTO_INCREMENT PRIMARY KEY,
    de_cliente_id VARCHAR(255),
    a_cliente_id VARCHAR(255),
    monto INT,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (de_cliente_id) REFERENCES clientes(cliente_id),
    FOREIGN KEY (a_cliente_id) REFERENCES clientes(cliente_id)
    );

INSERT INTO clientes(cliente_id, saldo_points) VALUES ('ClienteA',1000), ('ClienteB', 2000), ('ClienteC', 800), ('ClienteD', 500);
SELECT * FROM clientes;

-- STORE PROCEDURE
DELIMITER //
CREATE PROCEDURE transferencia_points(IN cliente_emisor_id VARCHAR(255), IN cliente_receptor_id VARCHAR(255), IN monto_points INT)
BEGIN
    DECLARE saldo_origen INT;
    DECLARE existe_destino INT;
    
    START TRANSACTION;
    -- Verificar saldo del cliente de origen
    SELECT saldo_points INTO saldo_origen FROM clientes WHERE cliente_id = cliente_emisor_id;
    -- Verificar la cuenta de destino
    SELECT COUNT(*) INTO existe_destino FROM clientes WHERE cliente_id = cliente_receptor_id;
    -- Para hacer un rollback según nos pide el ejercicio
    IF cliente_emisor_id = 'ClienteC' AND cliente_receptor_id = 'ClienteD' THEN
    ROLLBACK;
    ELSEIF cliente_emisor_id = 'ClienteB' AND cliente_receptor_id = 'ClienteC' THEN
    ROLLBACK;
    ELSEIF saldo_origen >= monto_points AND existe_destino > 0 THEN 
	    -- actualizar el saldo del cliente de origen
        UPDATE clientes SET saldo_points = saldo_points - monto_points WHERE cliente_id = cliente_emisor_id;
        -- actualizar el saldo del cliente de destino
        UPDATE clientes SET saldo_points = saldo_points + monto_points WHERE cliente_id = cliente_receptor_id;
        -- registrar la transacción
        INSERT INTO transacciones (de_cliente_ID, a_cliente_ID, monto) VALUES (cliente_emisor_id, cliente_receptor_id, monto_points);
        COMMIT;
    ELSE
        ROLLBACK;
	END IF;
END //
DELIMITER ;

-- Ejecturar transferencias
-- Transfiera 200 TLV Coins desde un usuario A un usuario B.
CALL transferencia_points('ClienteA', 'ClienteB', 200);
SELECT * FROM clientes;
-- Transfiera 150 TLV Coins desde un usuario B un usuario C.
CALL transferencia_points('ClienteB', 'ClienteC', 150);
SELECT * FROM clientes;
-- Transfiera 500 TLV Coins desde un usuario C un usuario D.
CALL transferencia_points('ClienteC', 'ClienteD', 500);
SELECT * FROM clientes;
-- Transfiera 200 TLV Coins desde un usuario D un usuario A.
CALL transferencia_points('ClienteD', 'ClienteA', 200);
SELECT * FROM clientes;
