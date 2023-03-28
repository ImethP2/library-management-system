def c22():
    #IMPORTING MODULES
    import mysql.connector as mysql
    db = mysql.connect(host="localhost", user="root", password="", database="doc334")
    mycursor = db.cursor(buffered=True)
    #GETTING DATA FROM THE USER
    comped=str(input("Which Chapter do you need to edit? (enter the Chapter Number)  ",))
    edit=str(input("What is the updated Chapter Starting Page Number? ",))
    #UPDATING THE DATA
    sql = "UPDATE bookChapters SET startingPageNo = %s WHERE chapterNo = %s"
    val = (edit, comped)
    mycursor.execute(sql, val)
    db.commit()
    print("data updated successfully")

    return
