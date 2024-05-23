from dtos import Hat
import sqlite3


class Hats:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, hat):
        self._conn.execute("""
               INSERT INTO hats (id, topping, supplier, quantity) VALUES (?, ?, ?, ?)
           """, [hat.id, hat.topping, hat.supplier, hat.quantity])

    def delete_quantity(self, hat_topping):
        self._conn.execute("""
                DELETE FROM hats WHERE topping=? AND quantity=0
        """, [hat_topping])

    def delete_all_quantity(self):
        self._conn.execute("""
        DELETE FROM hats WHERE quantity=0
        """)

    def find(self, hat_topping):
        c = self._conn.cursor()
        c.execute("""
                    SELECT hats.id FROM hats WHERE topping = ? AND quantity > 0 ORDER BY hats.supplier
                """, [hat_topping])
        if c is not None:
            return c.fetchone()  # ('1') => '1' => 1
        else:
            return (-1,)

    def reduce_quantity(self, id):
        c = self._conn.cursor()
        c.execute("""
                UPDATE hats SET quantity = (quantity - 1) WHERE id = ?
        """, [id])

    def contains(self, topping):
        c = self._conn.cursor()
        c.execute("""
                      SELECT * FROM hats WHERE topping = ? 
        """, [topping])
        return c.fetchone() is not None


class Suppliers:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, supplier):
        self._conn.execute("""
               INSERT INTO suppliers (id, name) VALUES (?, ?)
           """, [supplier.id, supplier.name])


class Orders:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, order):
        self._conn.execute("""
                       INSERT INTO orders (id, location, hat) VALUES (?, ?, ?)
                   """, [order.id, order.location, order.hat])

    def size(self):
        c = self._conn.cursor()
        c.execute("""
            SELECT * FROM orders;
        """)
        result = c.fetchall()
        return len(result)

    def order_output(self):
        c = self._conn.cursor()
        c.execute("""
            SELECT hats.topping, suppliers.name, orders.location 
            FROM orders 
            JOIN hats
            ON hats.id = orders.hat
            JOIN suppliers
            ON hats.supplier = suppliers.id
            ORDER BY orders.id
        """)
        return c.fetchall()
