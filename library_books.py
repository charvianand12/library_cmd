from database_conn import database_connection


def book_store():
    book_info = (
        (1234, "Don Quixote", 5),
        (1235, "Lord of the Rings", 3),
        (1236, "Harry Potter", 2),
        (1237, "Alice's Adventures in Wonderland", 1),
        (1238, "And Then There Were None", 3),
        (1239, "The Lion, the Witch, and the Wardrobe", 4),
        (1230, "Pinocchio", 10),
        (1231, "Catcher in the Rye", 5),
        (1232, "Fault In our Stars", 7),
        (1233, "Anne Of Green Gables", 6),
    )

    book_db, cur = database_connection()
    try:
        book_table = "CREATE TABLE IF NOT EXISTS books (Book_ID INT PRIMARY KEY, Book_Name TEXT, Inventory INT)"
        cur.execute(book_table)
        book_query = "INSERT OR IGNORE INTO books VALUES(?,?,?)"
        cur.executemany(book_query, book_info)
        book_db.commit()

    except:
        print("Error!!...table cannot be created")


def book_record():
    book_db, cur = database_connection()
    try:
        book_rec = "CREATE TABLE IF NOT EXISTS books_record (Reference_Number INT PRIMARY KEY, Student_Id Int, Book_ID INT, Status TEXT)"
        cur.execute(book_rec)

    except:
        print("Error!!...table cannot be created")


def addcolumn():
    book_db, cur = database_connection()
    try:
        book_rec = "ALTER TABLE books_record ADD Date_Returned DATE"
        cur.execute(book_rec)
        print("altered")

    except:
        print("Error!!...table cannot be altered")


# if __name__ == "__main__":
#     # book_store()
#     # book_record()
#     addcolumn()
