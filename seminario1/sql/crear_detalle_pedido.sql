drop table if exists detalle_pedido CASCADE;

CREATE TABLE IF NOT EXISTS detalle_pedido (
    cpedido INTEGER,  -- codigo del pedido en cuestion
    cproducto INTEGER, -- codigo del producto solicitado
    cantidad INTEGER NOT NULL, -- cantdad del producto en el pedido
    PRIMARY KEY (cpedido, cproducto), -- clave primaria 
    FOREIGN KEY (cpedido) REFERENCES pedido(cpedido), -- declaración explícita para foreign key
    FOREIGN KEY (cproducto) REFERENCES stock(cproducto) -- declaración explícita para foreign key
);

-- ejemplo de inserción
-- INSERT INTO detalle_pedido (cpedido, cproducto, cantidad) VALUES (1, 100, 5);
-- cpedido tiene que existir en tabla pedido y cproducto existir en tabla stock
 