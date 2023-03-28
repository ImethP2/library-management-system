def a1():
    #IMPORTING MODULES
    import mysql.connector as mysql
    db = mysql.connect(host="localhost", user="root", password="", database="doc334")
    mycursor = db.cursor(buffered=True)
    #GETTING THE INPUTS
    bn=str(input("input the book number : ",))
    t=str(input('input the title of the book : ',))
    
    print("\nplease select the relevent subject code\n")
    #SHOWING THE SUBJECTS TABLE
    sql="select * from subjects"
    mycursor.execute(sql)
    rows=mycursor.fetchall()
    for row in rows:
        for col in row:
            print('\t',col,'\t',end=' ')
        print()
    #ASKING IF A RELEVANT SUBJECT AVAILABLE IN THE TABLE
    sct=str(input('does this list include the subject related to your book? Y/N : ',))
    if sct=="Y" or sct=='y':
        #INSERTING THE OTHER DATA
        sc=str(input('\ninput the subject code : ',))
        aut=str(input('input the author of the book : ',))
        pub=str(input('input the publisher of the book : ',))
        pr=float(input('input the price of the book : ',))
        loc=str(input('input the location of the book : ',))
        chapc=int(input('input the number of chapters in the book : ',))
        sql = "INSERT INTO books (bookNo, title, subjectCode, author, publisher, price, location, chapterCount) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        val = (bn, t, sc, aut, pub, pr, loc, chapc)
        mycursor.execute(sql, val)

        db.commit()
        #REPEATING FOR CHAPTERS
        for cc in range (chapc):
            c1=cc+1
            #INPUTING DATA INTO THE BOOKCHAPTERS TABLE
            cn=str(input('input the chapter number : ',))
            ct=str(input('input the chapter title : ',))
            spn=str(input('input the starting page number : ',))
            epn=str(input('input the ending page number : ',))
            parac=int(input('input the paragraph count for the above paragraph : '))
            sql = "INSERT INTO bookChapters (bookNo, chapterNo, chapterTitle, startingPageNo, endingPageNo, paraCount) VALUES (%s, %s, %s, %s, %s, %s)"
            val = (bn, cn, ct, spn, epn, parac)
            mycursor.execute(sql, val)

            db.commit()
            #REPEATING FOR PARAGRAPH COUNT
            for pc in range (parac):
                p1=pc+1
                #INPUTING DATA INTO READ CHAPTERS TABLE
                rc=str(input(f'Enter the paragraph for chapter number {cn} paragraph number {p1} : ',))
                pn=str(cn)+str(p1)
                sql = "INSERT INTO readChapters (chapterNo, paraNo, readChap) VALUES (%s, %s, %s)"
                val = (bn, pn, rc)
                mycursor.execute(sql, val)

                db.commit()

        print(mycursor.rowcount, "record inserted.")
    elif sct=="N" or sct=='n':
        #ENTERING A NEW SUBJECT
        print("\nplease enter the subject with a subject code to continue\n")
        sc=str(input('input the subject code : ',))
        name=str(input('input the subject name : ',))
        sql = "INSERT INTO subjects (subjectCode, name) VALUES (%s, %s)"
        val = (sc, name)
        mycursor.execute(sql, val)
        db.commit()
        print(mycursor.rowcount, "record inserted to the Subjects table.\n")
        print("\nplease select the relevent subject code\n")
        sql="select * from subjects"
        mycursor.execute(sql)
        rows=mycursor.fetchall()
        for row in rows:
            for col in row:
                print('\t',col,'\t',end=' ')
            print()
        sc=str(input('\ninput the subject code : ',))
        mycursor.execute("select * from subjects")
        aut=str(input('input the author of the book : ',))
        pub=str(input('input the publisher of the book : ',))
        pr=str(input('input the price of the book : ',))
        loc=str(input('input the location of the book : ',))
        chapc=int(input('input the number of chapters in the book : ',))
        sql = "INSERT INTO books (bookNo, title, subjectCode, author, publisher, price, location, chapterCount) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        val = (bn, t, sc, aut, pub, pr, loc, chapc)
        mycursor.execute(sql, val)

        db.commit()

        for cc in range (chapc):
            c1=cc+1
            #cn=str(input('input the chapter ID : ',))
            cn=str(bn)+str(c1)
            ct=str(input('input the chapter title : ',))
            spn=str(input('input the starting page number : ',))
            epn=str(input('input the ending page number : ',))
            parac=int(input('input the paragraph count for the above paragraph : '))
            sql = "INSERT INTO bookChapters (bookNo, chapterNo, chapterTitle, startingPageNo, endingPageNo, paraCount) VALUES (%s, %s, %s, %s, %s, %s)"
            val = (bn, cn, ct, spn, epn, parac)
            mycursor.execute(sql, val)

            db.commit()
            for pc in range (parac):
                p1=pc+1
                rc=str(input(f'Enter the paragraph for chapter ID {cn} paragraph ID {p1} : ',))
                pn=str(cn)+str(p1)
                sql = "INSERT INTO readChapters (chapterNo, paraNo, readChap) VALUES (%s, %s, %s)"
                val = (cn, pn, rc)
                mycursor.execute(sql, val)

                db.commit()
        print(mycursor.rowcount, "record inserted.")
        return
