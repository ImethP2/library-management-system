def b1():
    #IMPORTING THE MODULES
    import mysql.connector as mysql
    db = mysql.connect(host="localhost", user="root", password="", database="doc334")
    mycursor = db.cursor(buffered=True)
    #PRINTING THE BOOKS TABLE
    mycursor.execute("select * from books")
    for td in mycursor:
        print(td)
    print()
    #GETTING THE BOOK NUMBER
    delb=str(input("input the book number that you need to delete : ",))
    #DELETING THE CHAPTERS
    sql = "DELETE bookChapters,readChapters FROM readChapters INNER JOIN bookChapters ON readChapters.chapterNo=bookChapters.chapterNo WHERE bookChapters.bookNo=%s"
    val=(delb,)
    mycursor.execute (sql,val)
    db.commit()
    #DELETING THE BOOKS
    sql= "delete from books where bookNo = %s"
    val = (delb,)
    mycursor.execute (sql,val)
    db.commit()
    print("data deleted successfully")

    return
