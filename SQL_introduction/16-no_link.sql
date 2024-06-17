-- ===========================================
-- Write a script that lists all records of the table second_table of the database 
-- auteur : BenBet21 17/06/2024
-- ============================================

SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;