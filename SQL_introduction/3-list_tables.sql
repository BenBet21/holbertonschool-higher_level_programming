-- =============================================
-- Write a script that lists all the tables of a database
-- auteur : BenBet21
-- ============================================
if [ $# -ne 1 ]; then
  echo "Usage: $0 <mysql>"
  exit 1
fi
DB_NAME="$1"
mysql -u your_username -p -e "USE $DB_NAME; SHOW TABLES;"
