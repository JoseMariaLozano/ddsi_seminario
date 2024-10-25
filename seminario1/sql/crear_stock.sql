drop table if exists stock CASCADE;

CREATE TABLE IF NOT EXISTS stock (
    cproducto INTEGER PRIMARY KEY, -- codigo del produco, clave primaria
    cantidad INTEGER -- cantidad del producto en stock 
);

-- ejemplos de inserción por defecto
-- INSERT INTO stock VALUES (1, 100);
-- INSERT INTO stock VALUES (1, 10);
-- INSERT INTO stock VALUES (1, 15);
-- INSERT INTO stock VALUES (1, 176);
-- INSERT INTO stock VALUES (1, 132);
-- INSERT INTO stock VALUES (1, 17);
-- INSERT INTO stock VALUES (1, 1000);
-- INSERT INTO stock VALUES (1, 6);
-- INSERT INTO stock VALUES (1, 1);
-- INSERT INTO stock VALUES (1, 100);

INSERT INTO stock VALUES 
    (1, 100),
    (2, 100),
    (3, 100),
    (4, 100),
    (5, 100),
    (6, 100),
    (7, 100),
    (8, 100),
    (9, 100),
    (10, 100);
