-- =============================================
-- Write a script that creates the table force_name
-- auteur : BenBet21
-- ============================================
USE hbtn_0d_2;
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
)