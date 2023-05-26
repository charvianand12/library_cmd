from database_conn import database_connection


def add_book():
    book_db, cur = database_connection()
    c = 0
    try:
        book_num = input("\n\nEnter the number of books to be added:  ")
        inp = int(book_num)
    except:
        print("\nError!!...Enter a valid Integer\n")
        if book_num == "":
            quit()
        else:
            add_book()

    else:
        for i in range(inp):
            check_id = "SELECT Book_ID from books"
            cur.execute(check_id)
            book_ids = cur.fetchall()

            try:
                book_id = int(input(f"\nEnter the Book ID for Book{i+1}:  "))
                book_id_tuple = (book_id,)
            except:
                print("\n Incorrect Book ID")
                # i=i-1

            else:
                if book_id_tuple in book_ids:
                    print("\n Book ID already exists..\n Please update Inventory..\n")

                else:
                    Book_name = input("\nEnter the name of the book:  ")
                    book_inv = int(input("\nEnter inventory:  "))
                    book_info = ((book_id, Book_name, book_inv),)
                    addbook_query = "INSERT OR IGNORE INTO books VALUES(?,?,?)"
                    cur.executemany(addbook_query, book_info)
                    book_db.commit()
                    c = c + 1
        # else:
        print(f"\n Hey Member!!.. {c} book(s) is/are added to the database\n")


def remove_book():
    book_db, cur = database_connection()
    book_id = int(input("\nEnter the book ID: "))
    check_id = "SELECT Book_ID from books"
    cur.execute(check_id)
    book_ids = cur.fetchall()
    book_id_tuple = (book_id,)

    if book_id_tuple in book_ids:
        name_query = "SELECT Book_Name FROM books WHERE BOOK_ID = ?"
        cur.execute(name_query, book_id_tuple)
        book_name = cur.fetchone()

        del_query = "DELETE FROM books WHERE Book_ID = ?"
        cur.execute(del_query, book_id_tuple)
        book_db.commit()
        print(f"\n{book_id}:{book_name[0]} has been removed from the database\n")

    else:
        print("\nBook Not Found\n")
        quit()


def update_book_inventory():
    book_db, cur = database_connection()
    book_id = int(input("\nEnter the book ID: "))

    check_id = "SELECT Book_ID from books"
    cur.execute(check_id)
    book_ids = cur.fetchall()
    book_id_tuple = (book_id,)

    if book_id_tuple in book_ids:
        book_inv = int(input("\n Enter the number: "))
        inv_query = "UPDATE books SET INVENTORY = ? WHERE Book_ID = ?"
        cur.execute(inv_query, [(book_inv), (book_id)])
        book_db.commit()
        print("\n Data Updated\n")
    else:
        print("\nNo book matches the given book id\n")


# if __name__=="__main__":
#     add_book()
#     remove_book()
#     update_book_inventory()
