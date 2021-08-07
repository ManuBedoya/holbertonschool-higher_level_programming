#!/usr/bin/python3
"""Module to list all cities
"""
import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect('localhost', sys.argv[1], sys.argv[2], sys.argv[3])
    cursor = db.cursor()

    sql = "SELECT cities.name FROM states INNER JOIN cities ON states.id = cities.state_id WHERE states.name='{}'ORDER BY states.id".format(sys.argv[4])

    cursor.execute(sql)
    data = cursor.fetchall()
    i = 0
    for i in range(len(data)):
        if (i == len(data) - 1):
            print(data[i][0])
        else:
            print(data[i][0], end=', ')
    db.close()
