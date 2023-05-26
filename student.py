from database_conn import database_connection


def student():
    student_info = (
        (9234, "Emily", "Em01"),
        (9235, "Gabriel", "Ga01"),
        (9236, "Cammillie", "Ca01"),
        (9237, "Raquel", "Ra01"),
        (9238, "Sergio", "Se01"),
        (9239, "Mindy", "Mi01"),
        (9230, "George", "Ge01"),
        (9231, "Bob", "Bo01"),
        (9232, "Noddy", "No01"),
        (9233, "Oswald", "Os01"),
    )

    # book_db = my_sql.connect("book_data.db")
    book_db, cur = database_connection()

    try:
        student_table = "CREATE TABLE IF NOT EXISTS student (Student_ID INT PRIMARY KEY, Student_Name TEXT, Student_Password TEXT)"
        cur.execute(student_table)
        student_query = "INSERT OR IGNORE INTO student VALUES(?,?,?)"
        cur.executemany(student_query, student_info)
        book_db.commit()

    except:
        print("Error!!...Table cannot be created")


student()
