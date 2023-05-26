from database_conn import database_connection


def register():
    name = input("\nEnter your Name:  ")
    if name.isdigit():
        print("\n Invalid Name. Please Try Again..\n")
        register()

    else:
        password = input("\nEnter your Password:  ")

        if name == "" or password == "":
            print("\nRegistration was unsuccessfull. Invalid Name or Password\n")

        else:
            book_db, cur = database_connection()
            max_id_query = "SELECT MAX (Student_ID) FROM student"
            cur.execute(max_id_query)
            max_Stu_id = cur.fetchone()
            # print(max_Stu_id,name,password)
            Stu_ID = max_Stu_id[0] + 1

            student_info = ((Stu_ID, name, password),)
            student_query = "INSERT OR IGNORE INTO student VALUES(?,?,?)"
            cur.executemany(student_query, student_info)
            book_db.commit()
            print(
                f"\n\nCongratulations!! You are registered successfully....\n Your Student ID is: {Stu_ID}.\n"
            )
