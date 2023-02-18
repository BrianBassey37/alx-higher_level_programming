#!/usr/bin/python3
"""script that takes in the name of a state as an argument and lists all
cities of that state"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], database=sys.argv[3])

    city = sys.argv[4]

    cursor = db.cursor()

    cursor.execute("SELECT cities.name FROM cities\
                    JOIN states ON cities.state_id = states.id\
                    WHERE states.name LIKE %s ORDER BY cities.id ASC", (city,))

    data = cursor.fetchall()

    print(", ".join(city[0] for city in data))

    cursor.close()
    db.close()
