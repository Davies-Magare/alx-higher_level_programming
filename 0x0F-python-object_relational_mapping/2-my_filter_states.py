#!/usr/bin/python3
"""Select all states with names corresponding to commandline argument"""

if __name__ == "__main__":
    import MySQLdb
    import sys
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], password=sys.argv[2],
                         database=sys.argv[3])
    cursor = db.cursor()
    new_str = """SELECT * FROM states WHERE name = '{}'
              ORDER BY id ASC""".format(sys.argv[4])
    cursor.execute(new_str)
    results = cursor.fetchall()
    for result in results:
        print(result)
    cursor.close()
    db.close()
