def c3():
    #IMPORTING MODULES
    import mysql.connector as mysql
    db = mysql.connect(host="localhost", user="root", password="", database="doc334")
    mycursor = db.cursor(buffered=True)
    #SHOWING THE SUBJECTS TABLE
    print("""\nSubject Name\n""")
    print("\tSubjects Table\t")
    print("\tSubject Code\t Name\t")
    sql="select * from subjects"
    mycursor.execute(sql)
    rows=mycursor.fetchall()
    for row in rows:
        for col in row:
            print('\t',col,'\t',end=' ')
        print()
    #GETTING DATA FROM THE USER
    ed=str(input("Which Subject do you need to edit? (enter the Subject Code)  ",))
    edit=str(input("What is the updated Subject Name? ",))
    #UPDATING THE DATA
    sql = "UPDATE subjects SET name = %s WHERE subjectCode = %s"
    val = (edit,ed)
    mycursor.execute(sql, val)
    db.commit()
    print("data updated successfully")

    return
