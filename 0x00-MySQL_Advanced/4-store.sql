-- SQL script to create a trigger that decreases the quantity of an item after adding a new order
-- Ensure the items and orders tables exist

CREATE TABLE IF NOT EXISTS items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    quantity INT NOT NULL
);

CREATE TABLE IF NOT EXISTS orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    item_id INT,
    quantity_ordered INT NOT NULL,
    FOREIGN KEY (item_id) REFERENCES items(id)
);

DROP TRIGGER IF EXISTS decrease_quantity_trigger;

CREATE TRIGGER decrease_quantity_trigger
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.quantity_ordered
    WHERE id = NEW.item_id;
END;
