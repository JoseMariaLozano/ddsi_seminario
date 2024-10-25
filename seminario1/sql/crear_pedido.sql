drop table if exists pedido CASCADE;

CREATE TABLE IF NOT EXISTS pedido (
    cpedido INTEGER PRIMARY KEY,
    ccliente SERIAL, -- el codigo del cliente es un entero autoincrementado (no tenemos una tabla de clientes)
    fecha_pedido DATE DEFAULT CURRENT-TIMESTAMP
);


