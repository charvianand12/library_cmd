from database_conn import database_connection


def check_count(stu_id):
    book_db, cur = database_connection()
    st = "Issued"

    count_query = (
        "SELECT COUNT(Book_ID) FROM books_record WHERE Student_Id = ? and Status = ?"
    )
    cur.execute(count_query, [(stu_id), (st)])
    count = cur.fetchall()
    return count[0][0]
