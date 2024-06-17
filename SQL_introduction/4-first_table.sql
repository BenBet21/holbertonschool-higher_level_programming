#!/bin/bash
-- ===========================================
-- Write a script that creates a table called first_table in the current database
-- auteur : BenBet21 17/06/2024
-- ============================================

if [ $# -ne 1 ]; then
  echo "Usage: $0 <database_name>"
  exit 1
fi
DB_NAME="$1"
mysql -u your_username -p -D "$DB_NAME" -e "CREATE TABLE IF NOT EXISTS first_table (id INT, name VARCHAR(256));"
