#!/usr/bin/python3
"""
Select all states from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    def main():
        """
        Connect to a MySQL server
        and list all states in the database
        using argv and the MySQLdb library
        """
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=db_name)

        cursor = db.cursor()

        cursor.execute("SELECT * FROM states ORDER BY id ASC")

        results = cursor.fetchall()

        for row in results:
            print(row)

        db.close()

if __name__ == "__main__":
    main()
