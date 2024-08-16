CREATE SCHEMA "gs";

CREATE TABLE gs.products(
    product_id SERIAL PRIMARY KEY NOT NULL ,
    name CHAR(100) NOT NULL,
    uom_id INT NOT NULL,
    price_per_unit DOUBLE PRECISION NOT NULL
);

CREATE TABLE gs.uom(
    uom_id SERIAL PRIMARY KEY NOT NULL,
    uom_name CHAR(45) NOT NULL
);

INSERT INTO gs.uom (uom_name) VALUES('each');

INSERT INTO gs.uom (uom_name) VALUES('each');

UPDATE gs.uom SET uom_name = 'kg' WHERE uom_id = 2;

ALTER TABLE gs.products ADD CONSTRAINT fk_uom_products FOREIGN KEY (uom_id) REFERENCES gs.uom(uom_id)

DROP TABLE gs.products;

CREATE TABLE gs.products(
    product_id SERIAL PRIMARY KEY NOT NULL ,
    name CHAR(100) NOT NULL,
    uom_id INT NOT NULL,
    price_per_unit DOUBLE PRECISION NOT NULL,
    CONSTRAINT fk_uom_products
    FOREIGN KEY (uom_id)
    REFERENCES gs.uom(uom_id)
    ON UPDATE RESTRICT
);

INSERT INTO gs.products (name, uom_id, price_per_unit) VALUES('toothpaste', 3, 30);

CREATE TABLE gs.orders(
    order_id SERIAL PRIMARY KEY NOT NULL,
    customer_name CHAR(100) NOT NULL,
    total DOUBLE PRECISION NOT NULL,
    datetime TIMESTAMP NOT NULL
);

CREATE TABLE gs.order_details(
    order_id INT PRIMARY KEY NOT NULL,
    product_id INT NOT NULL,
    quantity DOUBLE PRECISION NOT NULL,
    total_price DOUBLE PRECISION NOT NULL,
    CONSTRAINT fk_orders_order_details 
    FOREIGN KEY(order_id) 
    REFERENCES gs.orders(order_id)
    ON UPDATE RESTRICT,
    CONSTRAINT fk_products_order_details
    FOREIGN KEY(product_id)
    REFERENCES gs.products(product_id)
    ON UPDATE RESTRICT
);

INSERT INTO gs.orders(customer_name, total, datetime) VALUES('dhaval', 3000, LOCALTIMESTAMP);

INSERT INTO gs.order_details(order_id, product_id, quantity, total_price) VALUES(1, 1, 2, 60);