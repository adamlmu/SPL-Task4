import atexit
import sqlite3
import sys
from daos import Hats, Orders, Suppliers


class Repository:
    def __init__(self):
        self._conn = sqlite3.connect(sys.argv[4])
        self.hats = Hats(self._conn)
        self.suppliers = Suppliers(self._conn)
        self.orders = Orders(self._conn)

    def close(self):
        self._conn.commit()
        self._conn.close()

    def create_tables(self):
        self._conn.executescript("""
        CREATE TABLE hats(
            id          INTEGER     PRIMARY KEY,
            topping     TEXT        NOT NULL,
            supplier    INTEGER     REFERENCES suppliers(id), 
            quantity    INTEGER     NOT NULL 

        );

        CREATE TABLE suppliers(
            id       INTEGER     PRIMARY KEY,
            name     TEXT      NOT NULL
        );

        CREATE TABLE orders(
            id           INTEGER     PRIMARY KEY,
            location     TEXT        NOT NULL,
            hat          INTEGER     REFERENCES hats(id)
    
        );
    """)


repo = Repository()
