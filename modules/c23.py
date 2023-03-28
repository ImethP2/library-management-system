def c23():
    #IMPORTING THE MODULES
    import mysql.connector as mysql
    db = mysql.connect(host="localhost", user="root", password="", database="doc334")
    mycursor = db.cursor(buffered=True)
    #GETTING DATA FROM THE USER
    ed=str(input("Which Book do you need to edit? (enter the Book Number)  ",))
    comped=str(input("Which Chapter do you need to edit? (enter the Chapter Number)  ",))
    edit=str(input("What is the updated Chapter Ending Page Number? ",))
    #UPDATING THE DATA
    sql = "UPDATE bookChapters SET endingPageNo = %s WHERE bookNo = %s and chapterNo = %s"
    val = (edit,ed,comped)
    mycursor.execute(sql, val)
    db.commit()
    print("data updated successfully")

    return
