#!/usr/bin/python3
"""Uses database hbtn_0e_4_usa to list cities"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
    passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states ON states.id=cities.state_id")
    rows = cur.fetchall()
    for x in rows:
        print(x)
    cur.close()
    db.close()
