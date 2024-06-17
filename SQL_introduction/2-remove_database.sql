-- =============================================
-- delete database
-- auteur : BenBet21
-- ============================================
SET @database_name = 'hbtn_0c_0';
SET @drop_statement = CONCAT('DROP DATABASE IF EXISTS ', @database_name);
PREPARE stmt FROM @drop_statement;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;
