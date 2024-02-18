#!/usr/bin/python3
"""
This module demonstrates how to make a connection to
MySQLdb and execute a query.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host = "localhost", port = 3306,
                         user = sys.argv[1], password = sys.argv[2], database = sys.argv[3]);
    cursor = db.cursor()
    cursor.execute("SELECT id, name FROM states ORDER BY id ASC")
    results = cursor.fetchall()
    for result in results:
        print(result)
    cursor.close()
    db.close()

