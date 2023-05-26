import sqlite3 as my_sql


def database_connection():
    book_db = my_sql.connect("book_data.db")
    with book_db:
        cur = book_db.cursor()
    return book_db, cur


database_connection()
