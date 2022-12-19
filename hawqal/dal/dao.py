import sqlite3
import os


class Database:

    def __init__(self, path):
        self.databasePath = path

    def makeConnection(self):
        return sqlite3.connect(f"{self.databasePath}")
