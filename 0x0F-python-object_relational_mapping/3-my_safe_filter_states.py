#!/usr/bin/python3
"""
Select all states with names corresponding to commandline argument
Safe from SQL injection.
"""

if __name__ == "__main__":
    import MySQLdb
    import sys
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], password=sys.argv[2],
                         database=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("""SELECT * FROM states WHERE name = %s
                   ORDER BY id ASC""", (sys.argv[4],))
    results = cursor.fetchall()
    for result in results:
        print(result)
    cursor.close()
    db.close()
