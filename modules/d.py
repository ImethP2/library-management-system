def d1():
    #IMPORTING THE MODULES
    import mysql.connector as mysql
    db = mysql.connect(host="localhost", user="root", password="", database="doc334")
    mycursor = db.cursor(buffered=True)
    #GETTING THE DATA FROM THE USER
    search=str(input("Enter the Book Number : ",))
    #SHOWING THE DATA
    sql="select * from books where bookNo=%s"
    val=(search,)
    mycursor.execute(sql,val)
    rows=mycursor.fetchall()
    for row in rows:
        for col in row:
            print('\t',col,end=' ')
        print()

    


def d2():
    #IMPORTING THE MODULES
    import mysql.connector as mysql
    db = mysql.connect(host="localhost", user="root", password="", database="doc334")
    mycursor = db.cursor(buffered=True)
    #GETTING THE DATA FROM THE USER 
    search=str(input("Enter the Book Title : ",))
        #SHOWING THE DATA
    sql="select * from books where title=%s"
    val=(search,)
    mycursor.execute(sql,val)
    rows=mycursor.fetchall()
    for row in rows:
        for col in row:
            print('\t',col,end=' ')
        print()

    return


def d3():
    #IMPORTING THE MODULES
    import mysql.connector as mysql
    db = mysql.connect(host="localhost", user="root", password="", database="doc334")
    mycursor = db.cursor(buffered=True)
    #GETTING THE DATA FROM THE USER
    search=str(input("Enter the Book Author : ",))
        #SHOWING THE DATA
    sql="select * from books where author=%s"
    val=(search,)
    mycursor.execute(sql,val)
    rows=mycursor.fetchall()
    for row in rows:
        for col in row:
            print('\t',col,'\t',end=' ')
        print()

    return



def d4():
    #IMPORTING THE MODULES
    import mysql.connector as mysql
    db = mysql.connect(host="localhost", user="root", password="", database="doc334")
    mycursor = db.cursor(buffered=True)
    #GETTING THE DATA FROM THE USER 
    search=str(input("Enter the Book Publisher : ",))
        #SHOWING THE DATA    
    sql="select * from books where publisher=%s"
    val=(search,)
    mycursor.execute(sql,val)
    rows=mycursor.fetchall()
    for row in rows:
        for col in row:
            print('\t',col,'\t',end=' ')
        print()
                
    return


def d5():
    #IMPORTING THE MODULES
    import mysql.connector as mysql
    db = mysql.connect(host="localhost", user="root", password="", database="doc334")
    mycursor = db.cursor(buffered=True)
    #GETTING THE DATA FROM THE USER
    search=str(input("Enter the Subject Code : ",))
        #SHOWING THE DATA    
    sql="select * from books where subjectCode=%s"
    val=(search,)
    mycursor.execute(sql,val)
    rows=mycursor.fetchall()
    for row in rows:
        for col in row:
            print('\t',col,'\t',end=' ')
        print()

    return

