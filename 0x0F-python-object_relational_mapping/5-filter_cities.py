#!/usr/bin/python3
"""
List all cities from database hbtn_0e_4_usa
"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    def print_results(results):
        if len(results) == 0:
            return
        else:
            if len(results) == 1:
                print(results[0][0])
            else:
                print("{}, ".format(results[0][0]), end="")
            return print_results(results[1:])

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], password=sys.argv[2],
                         database=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("""SELECT name FROM cities WHERE state_id =
            (SELECT id FROM states WHERE name = %s)""", (sys.argv[4],))
    results = cursor.fetchall()
    print_results(results)
    cursor.close()
    db.close()
