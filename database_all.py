from database_conn import database_connection


def check_data():
    t = input(
        "\n Select a Database : \n1. Student Database \n2. Books Database \n3. Records\n"
    )
    if t == "1":
        table = "student"
    elif t == "2":
        table = "books"
    elif t == "3":
        table = "books_record"
    else:
        print("\nInvalid Selection\n")
        quit()

    query = f"SELECT * from {table}"

    _, cur = database_connection()
    cur.execute(query)
    data_list = cur.fetchall()
    print("\n")
    for i, item in enumerate(data_list):
        print(i + 1, item)
    print(f"\n{i+1} records found!!\n")


def books_due(s_id):
    Stu_id = (s_id,)
    _, cur = database_connection()
    book_id_query = "SELECT Book_ID FROM books_record WHERE Student_ID = ?"
    cur.execute(book_id_query, Stu_id)
    book_list = cur.fetchall()
    # print(book_list)

    if len(book_list) == 0:
        print("\n No book Issued.\n")

    else:
        print("\nYou need to return following book(s):")
        c = 0
        for i in book_list:
            b_id = i[0]
            status = "Issued"
            # print (i)
            bookname_query = "SELECT Book_Name FROM books WHERE Book_ID = ?"
            cur.execute(bookname_query, i)
            b_name = cur.fetchone()
            date_query = "SELECT DATE(Date_Issued, '+30 Day') FROM books_record WHERE Book_ID = ? AND Student_ID = ? AND Status = ?"
            cur.execute(date_query, [(b_id), (s_id), (status)])
            d = cur.fetchone()
            # print(d[0])
            if d is not None:
                c = c + 1
                print(f"\n {c}. {b_name[0]} by {d[0]}. \n")


if __name__=="__main__":
    books_due(9239)
