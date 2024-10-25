drop table if exists detalle_pedido CASCADE;

CREATE TABLE IF NOT EXISTS detalle_pedido (
    cpedido INTEGER REFERENCES pedido(cpedido),
    cproducto INTEGER REFERENCES stock(cproducto),
    cantidad INTEGER,
    PRIMARY KEY (cpedido, cproducto)
);

