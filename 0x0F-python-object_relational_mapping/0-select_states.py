#!/usr/bin/python3
"""Uses database hbtn_0e_0_usato list states"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()
    for x in rows:
        print(x)
    cur.close()
    db.close()
