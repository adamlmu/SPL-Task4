import sqlite3
import sys
import reading
import os
from repository import Repository


def main():
    if os.path.isfile('/home/spl211/Desktop/SPL_4/test_code/database.db'):
        os.remove('/home/spl211/Desktop/SPL_4/test_code/database.db')
    args = sys.argv
    repo = Repository()
    repo.create_tables()
    reading.read_and_init(args[1], repo)
    orders = reading.read_and_order(args[2], repo)
    reading.write_output(args[3], orders)
    repo.close()


if __name__ == '__main__':
    main()


