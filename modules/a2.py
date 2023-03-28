def a2():
    #IMPORTING MODULES
    import mysql.connector as mysql
    db = mysql.connect(host="localhost", user="root", password="", database="doc334")
    mycursor = db.cursor(buffered=True)
    #INPUTING DATA TO CHAPTERS TABLE
    bn=str(input('input the book number : ',))
    cn=str(input('input the chapter number : ',))
    ct=str(input('input the chapter title : ',))
    spn=str(input('input the starting page number : ',))
    epn=str(input('input the ending page number : ',))
    parac=int(input('input the paragraph count for the above chapter : '))
    sql = "INSERT INTO bookChapters (bookNo, chapterNo, chapterTitle, startingPageNo, endingPageNo, paraCount) VALUES (%s, %s, %s, %s, %s, %s)"
    ci=str(bn)+str(cn)
    val = (bn, ci, ct, spn, epn, parac)
    mycursor.execute(sql, val)
    #REPEATING FOR THE CHAPTER COUNT
    for pc in range (parac):
        p1=pc+1
        rc=str(input(f'Enter the paragraph for chapter number {cn} paragraph number {p1} : ',))
        pn=str(ci)+str(p1)
        sql = "INSERT INTO readChapters (chapterNo, paraNo, readChap) VALUES (%s, %s, %s)"
        val = (ci, pn, rc)
        mycursor.execute(sql, val)

        db.commit()

    print(mycursor.rowcount, "record inserted.")

    return

