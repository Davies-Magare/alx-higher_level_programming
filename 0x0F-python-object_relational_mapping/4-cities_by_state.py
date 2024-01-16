#!/usr/bin/python3
"""List all cities from database hbtn_0e_4_usa"""
import sys
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost",  port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = conn.cursor()
    query = "SELECT cities.id, cities.name, states.name \
             FROM cities LEFT JOIN states \
             ON cities.state_id = states.id \
             ORDER BY cities.id ASC"
    cur.execute(query)
    query_result = cur.fetchall()
    for row in query_result:
        print(row)
    cur.close()
    conn.close()
