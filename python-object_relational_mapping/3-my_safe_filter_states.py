#!/usr/bin/python3
"""script that takes in an argument and/
displays all values in the states table/
sans format pour éviter injection"""

import MySQLdb
import sys

if __name__ == "__main__":

    db = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )
    cursor = db.cursor()

    cursor.execute("""
        SELECT states.id, states.name
        FROM states
        WHERE BINARY states.name = %s
        ORDER BY states.id ASC
    """, (sys.argv[4],))

    rows = cursor.fetchall()
    for row in cursor:
        print(row)

    cursor.close()
    db.close()
