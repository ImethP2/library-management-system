def c12():
    #IMPORT MODULES
    import mysql.connector as mysql
    db = mysql.connect(host="localhost", user="root", password="", database="doc334")
    mycursor = db.cursor(buffered=True)

    print()
    #SHOWING THE SUBJECTS TABLE
    print("\tSubjects Table\t")
    sql="select * from subjects"
    mycursor.execute(sql,)
    rows=mycursor.fetchall()
    for row in rows:
        for col in row:
            print('\t',col,'\t',end=' ')
        print()
    #GETTING DATA FROM THE USER
    ed=str(input("Which Book do you need to edit? (enter the Book Number)  ",))
    edit=str(input("What is the updated Subject Code? ",))
    sql = "UPDATE books SET subjectCode = %s WHERE bookNo = %s"
    val = (edit,ed)
    mycursor.execute(sql, val)
    db.commit()
    print("data updated successfully")

    return
