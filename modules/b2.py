def b2():
    #IMPORTING MODULES
    import mysql.connector as mysql
    db = mysql.connect(host="localhost", user="root", password="", database="doc334")
    mycursor = db.cursor(buffered=True)
    #SHOWING THE 
    mycursor.execute("select * from bookChapters")
    for td in mycursor:
        print(td)
    print()
    #GETTING DATA 
    delc = str(input("input the chapter number that you need to delete : ",))
    #DELETING DATA FROM THE READ CHAPTER
    sql = "DELETE FROM readChapters WHERE chapterNo=%s"
    val = (delc, )
    mycursor.execute(sql, val)
    db.commit()
    #DELETING DATA FROM BOOK CHAPTERS
    sql = "DELETE FROM bookChapters WHERE chapterNo = %s"
    val = (delc,)
    mycursor.execute (sql,val)
    db.commit()
    
    print("data deleted successfully")

    return
