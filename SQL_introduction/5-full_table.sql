-- ===========================================
-- Write a script that prints the following description of the table first_table
-- auteur : BenBet21 17/06/2024
-- ============================================

USE hbtn_0c_0
SELECT 
    COLUMN_NAME, 
    COLUMN_TYPE, 
    IS_NULLABLE, 
    COLUMN_KEY 
FROM 
    information_schema.COLUMNS 
WHERE 
    TABLE_SCHEMA = 'hbtn_0c_0' 
    AND TABLE_NAME = 'first_table';