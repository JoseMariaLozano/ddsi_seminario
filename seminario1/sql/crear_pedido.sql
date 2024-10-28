drop table if exists pedido CASCADE;

CREATE TABLE IF NOT EXISTS pedido (
    cpedido INTEGER PRIMARY KEY, -- codigo del pedido, clave primaria
    ccliente INTEGER, -- el codigo del cliente es un entero
    fecha_pedido DATE DEFAULT CURRENT-TIMESTAMP -- no hay que introducir el dato al insertar en la tabla, se crea solo con la fecha de creación del pedido.
);


-- ejemplo de inserción 
-- INSERT INTO pedido (cpedido, ccliente) VALUES (1, 2);
