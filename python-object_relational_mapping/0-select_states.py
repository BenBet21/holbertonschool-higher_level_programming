#!/usr/bin/python3
"""script that lists all states from the database"""

import MySQLdb
import sys

if __name__ == "__main__":

    db = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )
    cur = db.cursor()

    cur.execute("SELECT states.id, states.name FROM states ORDER BY id ASC")
    for row in cur:
        print(row)
