#!/usr/bin/python3
"""Once again, write a script that takes in arguments and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument."""
import MySQLdb
import sys

"""Your script should take 4 arguments: mysql username, mysql password,
database name and state name searched (safe from MySQL injection)
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by states.id
Results must be displayed as they are in the example below
Your code should not be executed when imported """

if __name__ == "__main__":
    state = sys.argv[4]
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], database=sys.argv[3])

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states\
                    WHERE name LIKE %s ORDER BY id ASC", (state,))

    data = cursor.fetchall()

    for state in data:
        print(state)

    cursor.close()
    db.close()
