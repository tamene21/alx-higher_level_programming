#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa"""
if __name == '__name__':
    import MYSQLdb
    import sys

    db = MYSQLdb.connect(host= 'localhost', port= 3306, user=sys.argv[1], passwd=sys.argv[2],db=sys.argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC;")
    rows = cur.fetchall()
    for row in rows:
        print(row)
