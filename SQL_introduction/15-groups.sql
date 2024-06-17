-- ===========================================
-- Write a script that lists the number of records with the same score in the table
-- auteur : BenBet21 17/06/2024
-- ============================================

SELECT score, COUNT(score) AS number FROM second_table GROUP BY score ORDER BY number DESC;