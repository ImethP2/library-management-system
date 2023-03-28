def b3():
    #IMPORTING MODULES
    import mysql.connector as mysql
    db = mysql.connect(host="localhost", user="root", password="", database="doc334")
    mycursor = db.cursor(buffered=True)
    #SHOWING THE SUBJECT TABLE
    mycursor.execute("select * from subjects")
    for td in mycursor:
        print(td)
    print()
    #DELETING DATA FROM READ CHAPTERS TABLE, BOOK CHAPTERS TABLE AND THE BOOKS TABLE
    dels=str(input("input the subject code that you need to delete : ",))
    sql = "DELETE readChapters,bookChapters,books FROM bookChapters INNER JOIN readChapters ON bookChapters.chapterNo=readChapters.chapterNo INNER JOIN books ON bookChapters.bookNo=books.bookNo WHERE bookChapters.bookNo=books.bookNo AND books.subjectCode=%s"
    val = (dels,)
    mycursor.execute (sql,val)
    db.commit()
    #DELETING DATA FROM THE SUBJECT CODE

    sql1= "delete from subjects where subjectCode = %s"
    val1 = (dels,)
    mycursor.execute (sql1,val1)
    db.commit()
    print("data deleted successfully")

    return
