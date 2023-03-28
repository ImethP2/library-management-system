def a3():
    #IMPORTING MODULES
    import mysql.connector as mysql
    db = mysql.connect(host="localhost", user="root", password="", database="doc334")
    mycursor = db.cursor(buffered=True)
    #INPUTING THE SUBJECT CODE
    sc=str(input('input the subject code : ',))
    name=str(input('input the subject name : ',))
    sql = "INSERT INTO subjects (subjectCode, name) VALUES (%s, %s)"
    val = (sc, name)
    mycursor.execute(sql, val)

    db.commit()

    print(mycursor.rowcount, "record inserted.")

    return
