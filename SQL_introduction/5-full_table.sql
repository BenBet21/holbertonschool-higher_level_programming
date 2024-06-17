-- ===========================================
-- Write a script that prints the following description of the table first_table
-- auteur : BenBet21 17/06/2024
-- ============================================

USE information_schema;
SELECT 
    COLUMN_NAME, 
    COLUMN_TYPE, 
    IS_NULLABLE, 
    COLUMN_KEY 
FROM 
    COLUMNS 
WHERE 
    TABLE_SCHEMA = DATABASE() 
    SHOW CREATE TABLE `first_table`;