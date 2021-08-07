#!/usr/bin/python3
"""Module to list all cities
"""
import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect('localhost', sys.argv[1], sys.argv[2], sys.argv[3])
    cursor = db.cursor()

    sql = "SELECT cities.id, cities.name, states.name FROM states INNER JOIN cities ON states.id = cities.state_id ORDER BY states.id"

    cursor.execute(sql)
    data = cursor.fetchall()
    for item in data:
        print(item)
    db.close()
