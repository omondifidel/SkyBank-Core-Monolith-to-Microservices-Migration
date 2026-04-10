CREATE TABLE accounts (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    balance DECIMAL(15, 2)
);

INSERT INTO accounts (name, balance) VALUES ('Sky User', 5000.00);
INSERT INTO accounts (name, balance) VALUES ('Recipient User', 1000.00);