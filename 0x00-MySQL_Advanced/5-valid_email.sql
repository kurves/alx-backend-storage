-- SQL script to create a trigger that resets the valid_email attribute 
-- only when the email has been changed

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL,
    valid_email BOOLEAN DEFAULT TRUE
);

DROP TRIGGER IF EXISTS reset_valid_email_trigger;

CREATE TRIGGER reset_valid_email_trigger
AFTER UPDATE ON users
FOR EACH ROW
BEGIN
    IF OLD.email <> NEW.email THEN
        UPDATE users
        SET valid_email = FALSE
        WHERE id = NEW.id;
    END IF;
END;

