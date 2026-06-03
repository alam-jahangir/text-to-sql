import sqlite3

class SqliteCon:

    def __init__(self):
        self.conn = None
        self.cursor = None

    def connect(self):
        self.conn = sqlite3.connect("sample.db")
        self.cursor = self.conn.cursor()

    def execute(self, query: str):
        if self.conn is None:
            self.connect()

        for row in self.cursor.execute(query):
            yield row

    def close(self) -> None:
        if self.conn is not None:
           self.conn.close()