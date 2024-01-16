#!/usr/bin/python3
import sys
import MySQLdb
""" This script lists all states from the database hbtn_0e_0_usa """

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost",  port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id")
    query_result = cur.fetchall()
    for row in query_result:
        print(row)
    cur.close
    conn.close
