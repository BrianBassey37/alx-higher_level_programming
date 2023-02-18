#!/usr/bin/python3
"""script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument"""

import MySQLdb
import sys

if __name__ == "__main__":
    state = sys.argv[4]
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], database=sys.argv[3])

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name='{}'\
                    ORDER BY id ASC".format(state))

    data = cursor.fetchall()

    for state1 in data:
        if state1[1] == state:
            print(state1)

    cursor.close()
    db.close()
