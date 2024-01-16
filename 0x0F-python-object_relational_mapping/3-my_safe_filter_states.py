#!/usr/bin/python3
"""List all cities in database using a query safe from a sql injection"""
import sys
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost",  port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = conn.cursor()
    query = "SELECT * FROM states WHERE name = %s \
             ORDER BY states.id ASC"
    cur.execute(query, (sys.argv[4],))
    query_result = cur.fetchall()
    for row in query_result:
        print(row)
    cur.close()
    conn.close()
