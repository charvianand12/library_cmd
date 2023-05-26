from database_conn import database_connection
import books_update
import check_record
import register_student
import getpass
import add_del_books
import database_all


def book_list(cur, stu_id):
    book_list_query = "SELECT Book_ID, Book_Name FROM books WHERE Inventory >= 1"
    cur.execute(book_list_query)
    available_book = cur.fetchall()
    print("\n The books available in the library are: \nBook ID, Book Name\n")
    for i in available_book:
        print(i)
    # print(type(available_book))
    # s = ",".join(available_book)
    # print(s)
    issuebook(cur, stu_id)


def issuebook(cur, stu_id):
    try:
        bk_id = input("\n enter the book id :  ")
        b_id = int(bk_id)
    except:
        if bk_id == "":
            quit()
        else:
            print("\nInvalid Book ID\n")
            book_list(cur, stu_id)

    else:
        bookid = (b_id,)
        book_id_query = "SELECT Book_ID FROM books WHERE Inventory >= 1"
        cur.execute(book_id_query)
        available_bookid = cur.fetchall()
        ref_no = str(stu_id) + str(b_id)

        if bookid in available_bookid:
            print(
                f"\n\nYou can collect the book from the counter..\n\n Your reference number is: {ref_no}. You need to return the book within 30 days \n"
            )
            books_update.update_inv(b_id)
            books_update.update_table(stu_id, b_id, int(ref_no))
            # print("data updated")

        else:
            print("\nBook ID did not match.. Enter correct ID...\n")
            issuebook(cur, stu_id)


def return_book(cur, stu_id):
    reference_num = int(input("\n enter the reference number:  "))
    ref_num = (reference_num,)

    book_ref_query = "SELECT Reference_Number FROM books_record"
    cur.execute(book_ref_query)
    return_ref = cur.fetchall()

    if ref_num in return_ref:
        books_update.return_update_inv(reference_num)
        books_update.return_update_table(reference_num)
        print("\n Request Accepted..\n")

    else:
        print("\nNo book issued with this reference number.. Please Try Again\n")
        return_book(cur, stu_id)


def check_key(counter):
    key = input("\nEnter the key: ")
    key_check = lambda k: k == "1111"
    res = key_check(key)
    if res is True:
        database_all.check_data()
    else:
        while counter != 1:
            print(f"Wrong key...  {counter-1} attempt(s) left")
            counter = counter - 1
            check_key(counter)
        if counter == 1:
            quit()


def staff_menu():
    inp = input(
        "\n\n Please select your requirement: \n1: Add books \n2: Delete a book \n3: Update Inventory \n4: Check Database\n"
    )
    if inp == "1":
        add_del_books.add_book()
    elif inp == "2":
        add_del_books.remove_book()
    elif inp == "3":
        add_del_books.update_book_inventory()
    elif inp == "4":
        print("\nKey Required. You have 3 attempts!!\n")
        check_key(3)

    else:
        print("\nInvalid selection\n")
        quit()


def student_menu(stu_id, cur):
    inp = input("\n\n Enter '1' to Issue a book or '2' to Return a book\n")
    if inp == "1":
        count = check_record.check_count(stu_id)
        if count < 3:
            book_list(cur, stu_id)
        elif count == 3:
            print("\nLimit Exhausted....\n")
        else:
            print("Error!!!")

    elif inp == "2":
        return_book(cur, stu_id)
    else:
        print("\nInvalid selection\n")


def check_staff_password(pas, cur):
    if pas == "Library@":
        print("\nWelcome Staff..\n")
        staff_menu()
    else:
        print("\n Invalid Credentials..!!\n")


def check_password(pas, cur):
    pas = (pas,)

    pas_query = "SELECT Student_password from student"
    data_query = "SELECT * from student where Student_password = ?"

    cur.execute(pas_query)
    pass_list = cur.fetchall()

    if pas in pass_list:
        cur.execute(data_query, pas)
        data_list = cur.fetchall()
        print("Welcome!!, ", data_list[0][1])
        database_all.books_due(data_list[0][0])
        student_menu(data_list[0][0], cur)

    else:
        print("Wrong Password!!.... Please Try Again")
        main()


def main():
    _, cur = database_connection()

    print("\n\n*******The PYTHON Library welcomes you*******\n\n")
    inp = input("Please select:\n 1. Staff \n 2. Student\n 3. Guest\n 0. Exit\n\n")

    if inp == "1":
        password = getpass.getpass(prompt="\n Enter your Password:  ")
        # password = input("\n\nPlease Enter your Password to continue:\n\n")
        check_staff_password(password, cur)

    elif inp == "2":
        password = getpass.getpass(prompt="\n Enter your Password:  ")
        # password = input("\n\nPlease Enter your Password to continue:\n\n")
        check_password(password, cur)

    elif inp == "3":
        print("\nPlease register yourself\n\n")
        register_student.register()

    elif (inp == "0") or (inp == ""):
        quit()

    else:
        print("Invalid Option..\n")
        main()


if __name__ == "__main__":
    main()
