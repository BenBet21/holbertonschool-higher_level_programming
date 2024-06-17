-- ===========================================
-- Write a script that lists the number of records with the same score in the table
-- auteur : BenBet21 17/06/2024
-- ============================================

SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;