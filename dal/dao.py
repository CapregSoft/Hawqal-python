import sqlite3
import os

def create_cursor():
    dirname = os.path.dirname(__file__)
    file_name = os.path.join(dirname, '..', 'database', 'hawqalDB.sqlite')
    with open(file_name, 'r', encoding="utf8"):
        database = sqlite3.connect(file_name)
        cursor = database.cursor()
    return cursor