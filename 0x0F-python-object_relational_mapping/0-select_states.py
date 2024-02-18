#!/usr/bin/python3
"""Make a connection to MySQLdb and execute a query."""

if __name__ == "__main__":
    import MySQLdb
    import sys
    db = MySQLdb.connect(host = "localhost", port = 3306,
                         user = sys.argv[1], password = sys.argv[2], database = sys.argv[3]);
    cursor = db.cursor()
    cursor.execute("SELECT id, name FROM states ORDER BY id ASC")
    results = cursor.fetchall()
    for result in results:
        print(result)
    cursor.close()
    db.close()

