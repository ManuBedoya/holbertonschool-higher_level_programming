#!/usr/bin/python3
"""Module to find state
"""
import MySQLdb
import sys


if __name__ == '__main__':
    db = MySQLdb.connect('localhost', sys.argv[1], sys.argv[2], sys.argv[3])
    cursor = db.cursor()

    sql = "SELECT * FROM states WHERE name='{}'".format(sys.argv[4])
    cursor.execute(sql)
    data = cursor.fetchall()
    for item in data:
        print(item)

    db.close()
