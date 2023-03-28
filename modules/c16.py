def c16():
    #IMPORTING THE MODULES
    import mysql.connector as mysql
    db = mysql.connect(host="localhost", user="root", password="", database="doc334")
    mycursor = db.cursor(buffered=True)
    #GETTING DATA FROM THE USER
    ed=str(input("Which Book do you need to edit? (enter the Book Number)  ",))
    edit=str(input("What is the updated Book Location? ",))
    #UPDATING THE DATA
    sql = "UPDATE books SET location = %s WHERE bookNo = %s"
    val = (edit,ed)
    mycursor.execute(sql, val)
    db.commit()
    print("data updated successfully")

    return
