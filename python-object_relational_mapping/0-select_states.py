#!/usr/bin/python3
import MySQLdb
import sys

username = sys.argv[1]
password = sys.argv[2]
db_name = sys.argv[3]


def main():
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=db_name)
    cursor = db.cursor()

    cursor.execute("SELECT * FROM states ORDER BY name ASC")

    results = cursor.fetchall()

    for row in results:
        print(row)

    db.close()


if __name__ == "__main__":
    main()
