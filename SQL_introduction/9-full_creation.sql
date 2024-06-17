ip addr show eth0 | grep -oP '(?<=inet\s)\d+(\.\d+){3}'-- ===========================================
-- Write a script that creates a table second_table in the database 
-- auteur : BenBet21 17/06/2024
-- ============================================

CREATE TABLE IF NOT EXISTS second_table(
    id INT PRIMARY KEY,
    name VARCHAR(256),
    score INT
);

INSERT INTO second_table(id, name, score) VALUES
(1, 'John', 10),
(2, 'Alex', 3),
(3, 'Bob', 14),
(4, 'George', 8);