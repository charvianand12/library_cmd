from database_conn import database_connection
import datetime


def update_inv(b_id):
    b_id_tuple = (b_id,)
    book_db, cur = database_connection()

    inv_query = "SELECT Inventory FROM books WHERE Book_Id = ?"
    cur.execute(inv_query, b_id_tuple)
    ref_bookid = cur.fetchall()
    inv = ref_bookid[0][0] - 1
    # print (inv)
    update_query = "UPDATE books SET Inventory = ? WHERE Book_Id = ? "
    cur.execute(update_query, [(inv), (b_id)])
    book_db.commit()
    book_db.close()


def update_table(stu_id, b_id, ref_num):
    book_db, cur = database_connection()

    d = datetime.date.today()
    table_info = ((ref_num, stu_id, b_id, "Issued", d, ""),)
    insert_record_query = "INSERT OR IGNORE INTO books_record VALUES(?,?,?,?,?,?)"
    cur.executemany(insert_record_query, table_info)
    book_db.commit()
    book_db.close()


def return_update_inv(ref_num):
    ref_tuple = (ref_num,)
    book_db, cur = database_connection()
    ref_query = "SELECT Book_ID FROM books_record WHERE Reference_Number = ?"
    cur.execute(ref_query, ref_tuple)
    ref_bookid = cur.fetchall()
    return_book_id = ref_bookid[0][0]
    return_book_id_tuple = (ref_bookid[0][0],)

    return_inv_query = "SELECT Inventory FROM books WHERE Book_Id = ?"
    cur.execute(return_inv_query, return_book_id_tuple)
    return_inv = cur.fetchall()
    inv = return_inv[0][0] + 1

    update_query = "UPDATE books SET Inventory = ? WHERE Book_Id = ? "
    cur.execute(update_query, [(inv), return_book_id])
    book_db.commit()
    book_db.close()


def return_update_table(ref_num):
    book_db, cur = database_connection()
    r = "returned"
    d = datetime.date.today()
    Update_record_query = "UPDATE books_record SET Status = ?, Date_Returned = ? WHERE Reference_Number = ?"
    cur.execute(Update_record_query, [(r), (d), (ref_num)])
    book_db.commit()
    book_db.close()

# if __name__ == "__main__":
    