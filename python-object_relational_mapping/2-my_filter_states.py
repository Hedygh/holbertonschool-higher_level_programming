#!/usr/bin/python3
"""Lists states matching the given name."""

import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8"
    )

    cur = db.cursor()
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(
        sys.argv[4]
    )
    cur.execute(query)

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
