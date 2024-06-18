-- =============================================
-- Write a script that creates the table id_not_null
-- auteur : BenBet21
-- ============================================
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);