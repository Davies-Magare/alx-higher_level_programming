#!/usr/bin/python3
"""List all cities in state passed in command line argument"""
import sys
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost",  port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = conn.cursor()
    query = "SELECT name from cities WHERE state_id IN \
             (SELECT id from states WHERE name = %s)"
    cur.execute(query, (sys.argv[4],))
    query_result = cur.fetchall()
    if not query_result:
        print()
    else:
        result_list = []
        for row in query_result:
            result_list.append(row[0])
        for city in result_list:
            if city != result_list[-1]:
                print("{}, ".format(city), end="")
            else:
                print(city)
    cur.close()
    conn.close()
