import sqlite3
import os


def databaseConnection():
    dirname = os.path.dirname(__file__)
    file_name = os.path.join(dirname, '..', 'database', 'hawqalDB.sqlite')
    with open(file_name, 'r', encoding="utf-8"):
        database = sqlite3.connect(file_name)
        cursor = database.cursor()
        cursor.execute("pragma encoding")
    return cursor
