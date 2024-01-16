#!/usr/bin/python3
"""List all cities in database that match commandline argument"""
import sys
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost",  port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = conn.cursor()
    query = "SELECT * FROM states WHERE name = '{}' \
            ORDER BY states.id ASC".format(sys.argv[4])
    cur.execute(query)
    query_result = cur.fetchall()
    for row in query_result:
        print(row)
    cur.close()
    conn.close()
