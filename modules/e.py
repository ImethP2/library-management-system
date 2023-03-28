def e():
    #IMPORTING THE MODULES
    import mysql.connector as mysql
    db = mysql.connect(host="localhost", user="root", password="", database="doc334")
    mycursor = db.cursor(buffered=True)
    cread="Y"
    
    while cread=="Y" or cread =='y':
        #GETIING DATA FROM THE USER
        readc=str(input("Enter the Chapter Number : ",))
        #SHOWING THE CHAPTER
        sql="select readChap from readChapters where chapterNo=%s "
        val=(readc,)
        mycursor.execute(sql,val)
        rows=mycursor.fetchall()
        for row in rows:
            for col in row:
                print('\t',col,'\t',end=' ')
            print()
        #ASKING FOR SHOW ANOTHER CHAPTER
        cread=str(input("do you want to read another chapter? Y/N : ",))
        if cread!='y' and cread!="Y" and cread !='n' and cread !="N" :
            print('enter a valid input')
            

        
    return
