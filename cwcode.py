#IMPORTING MODULES
import mysql.connector as mysql
import modules.a1
import modules.a2
import modules.a3
import modules.b1
import modules.b2
import modules.b3
import modules.c11
import modules.c12
import modules.c13
import modules.c14
import modules.c15
import modules.c16
import modules.c21
import modules.c22
import modules.c23
import modules.c3
import modules.d
import modules.e
#ASSIGNING VARIABLES
db = mysql.connect(host="localhost", user="root", password="", database="doc334")

x=0
bn=0
t=0
td=0
sc=0
aut=0
pub=0
pr=0
loc=0
chapc=0
cc=0
sql=0
val=0
cn=0
spn=0
epn=0
sc=0
name=0
sct=0
dr=0
et=0
ed=0
comped=0
edit=0
search=0
cont=True
contserv="Y"
cread="Y"

mycursor = db.cursor(buffered=True)
print("""-------------------------WELCOME TO LIBRARY MANAGEMENT PROGRAM-------------------------

""")

#LOOPING THE WHOLE PROGRAM
while cont==True:
    contserv="Y"
    print("""MENU\r
a) Insert data into a table
b) Delete data from a table
c) Edit a data row
d) Search
e) Read the book
f) Exit\n""")
    x=input("what service do you need? ",)
#INSERTING DATA
    if x=="a" or x=="A":
        print("""\nTable Menu\n
1)Books
2)Book Chapters
3)Subject Code\n""")
        tb=input("For what table do you need to enter data? ",)
        print()
        #INSERTING A BOOK
        if tb=="1":
            while contserv=="y" or contserv=="Y":
                #CALLING THE MODULES
                modules.a1.a1()
                #ASKING TO REPEAT THE SERVICE
                contserv=str(input("do you want to continue this service? Y/N   ",))
                if contserv!="Y" and contserv!="y" and contserv!="N" and contserv!='n':
                    print("error input")
                if contserv == "N" or contserv=='n':
                    #ASKING TO REPEAT THE SOFTWARE
                    continp=str(input("Do you still want to continue? Y/N  ",))
                    if continp=="Y" or continp=='y':
                        cont=True
                        print()
                    elif continp=="N" or continp=='n':
                        cont=False
                    else:
                        print("please enter a valid input")
                        cont=False
                    
         #INSERTING A BOOK CHAPTER       
        elif tb=='2':
            while contserv=="y" or contserv=="Y":
                                #CALLING THE MODULES 
                modules.a2.a2()

                contserv=str(input("do you want to continue this service? Y/N   ",))
                if contserv!="Y" and contserv!="y" and contserv!="N" and contserv!='n':
                    print("error input")
                if contserv == "N" or contserv=='n':
                        
                    continp=str(input("Do you still want to continue? Y/N  ",))
                    if continp=="Y" or continp=='y':
                        cont=True
                        print()
                    elif continp=="N" or continp=='n':
                        cont=False
                    else:
                        print("please enter a valid input")
                        cont=False

        #INSERTING A SUBJECT CODE
        elif tb=='3':
            while contserv=="y" or contserv=="Y":
                #CALLING THE MODULES            
                modules.a3.a3()
                
                contserv=str(input("do you want to continue this service? Y/N   ",))
                if contserv!="Y" and contserv!="y" and contserv!="N" and contserv!='n':
                    print("error input")
                if contserv == "N" or contserv=='n':
                        
                    continp=str(input("Do you still want to continue? Y/N  ",))
                    if continp=="Y" or continp=='y':
                        cont=True
                        print()
                    elif continp=="N" or continp=='n':
                        cont=False
                    else:
                        print("please enter a valid input")
                        cont=False

        else:
            print("please enter a valid input")
    #DELETING DATA
    elif x=="B" or x=="b":
        print("""\nTable Menu\n
1)Books
2)Book Chapters
3)Subject Code\n""")
        tb=str(input("From which table do you need to delete data? ",))
        print()
        #DELETING A BOOK
        if tb=="1":
            while contserv=="y" or contserv=="Y":

                #CALLING THE MODULE
                modules.b1.b1()
               
                contserv=str(input("do you want to continue this service? Y/N   ",))
                if contserv!="Y" and contserv!="y" and contserv!="N" and contserv!='n':
                    print("error input")
                if contserv == "N" or contserv=='n':
                        
                    continp=str(input("Do you still want to continue? Y/N  ",))
                    if continp=="Y" or continp=='y':
                        cont=True
                        print()
                    elif continp=="N" or continp=='n':
                        cont=False
                    else:
                        print("please enter a valid input")
                        cont=False
        #DELETING A BOOK CHAPTER
        elif tb=="2":
            while contserv=="y" or contserv=="Y":
#CALLING THE MODULE
                modules.b2.b2()
                
                contserv=str(input("do you want to continue this service? Y/N   ",))
                if contserv!="Y" and contserv!="y" and contserv!="N" and contserv!='n':
                    print("error input")
                if contserv == "N" or contserv=='n':
                        
                    continp=str(input("Do you still want to continue? Y/N  ",))
                    if continp=="Y" or continp=='y':
                        cont=True
                        print()
                    elif continp=="N" or continp=='n':
                        cont=False
                    else:
                        print("please enter a valid input")
                        cont=False
        #DELETING A SUBJECT
        elif tb=="3":
            while contserv=="y" or contserv=="Y":
#CALLING THE MODULE
                modules.b3.b3()
                
                contserv=str(input("do you want to continue this service? Y/N   ",))
                if contserv!="Y" and contserv!="y" and contserv!="N" and contserv!='n':
                    print("error input")
                if contserv == "N" or contserv=='n':
                        
                    continp=str(input("Do you still want to continue? Y/N  ",))
                    if continp=="Y" or continp=='y':
                        cont=True
                        print()
                    elif continp=="N" or continp=='n':
                        cont=False
                    else:
                        print("please enter a valid input")
                        cont=False

        else:
            print("please enter a valid input")
    #EDDITING DATA
    elif x=="C" or x=="c":
        print("""\nTable Menu\n
1) Books
2) Book Chapters
3) Subject Code\n""")
        tb=input("In which table do you need to edit data? ",)
        print()
        #EDITING BOOK DATA
        if tb=="1":
            print("""\nBook Table Menu\n
1) Book Title
2) Subject Code
3) Author
4) Publisher
5) Price
6) Location\n""")
            et=str(input("In which column do you need to edit data? ",))
            print()
            print("\tBooks Table\t")
            sql="select * from books"
            mycursor.execute(sql)
            rows=mycursor.fetchall()
            for row in rows:
                for col in row:
                    print('\t',col,end=' ')
                print()
            #EDITING THE BOOK TITLE
            if et=='1':
                while contserv=="y" or contserv=="Y":
#CALLING THE MODULE
                    modules.c11.c11()
                    
                    contserv=str(input("do you want to continue this service? Y/N   ",))
                    if contserv!="Y" and contserv!="y" and contserv!="N" and contserv!='n':
                        print("error input")
                    if contserv == "N" or contserv=='n':
                            
                        continp=str(input("Do you still want to continue? Y/N  ",))
                        if continp=="Y" or continp=='y':
                            cont=True
                            print()
                        elif continp=="N" or continp=='n':
                            cont=False
                        else:
                            print("please enter a valid input")
                            cont=False
            #EDITING THE BOOK SUBJECT
            elif et=='2':
                while contserv=="y" or contserv=="Y":
#CALLING THE MODULE
                    modules.c12.c12()
                    
                    contserv=str(input("do you want to continue this service? Y/N   ",))
                    if contserv!="Y" and contserv!="y" and contserv!="N" and contserv!='n':
                        print("error input")
                    if contserv == "N" or contserv=='n':
                            
                        continp=str(input("Do you still want to continue? Y/N  ",))
                        if continp=="Y" or continp=='y':
                            cont=True
                            print()
                        elif continp=="N" or continp=='n':
                            cont=False
                        else:
                            print("please enter a valid input")
                            cont=False
            #EDITING THE BOOK AUTHOR 
            elif et=='3':
                while contserv=="y" or contserv=="Y":

                    modules.c13.c13()
                    
                    contserv=str(input("do you want to continue this service? Y/N   ",))
                    if contserv!="Y" and contserv!="y" and contserv!="N" and contserv!='n':
                        print("error input")
                    if contserv == "N" or contserv=='n':
                            
                        continp=str(input("Do you still want to continue? Y/N  ",))
                        if continp=="Y" or continp=='y':
                            cont=True
                            print()
                        elif continp=="N" or continp=='n':
                            cont=False
                        else:
                            print("please enter a valid input")
                            cont=False
            #EDITING THE BOOK PUBLISHER
            elif et=='4':
                while contserv=="y" or contserv=="Y":
#CALLING THE MODULE
                    modules.c14.c14()
                    
                    contserv=str(input("do you want to continue this service? Y/N   ",))
                    if contserv!="Y" and contserv!="y" and contserv!="N" and contserv!='n':
                        print("error input")
                    if contserv == "N" or contserv=='n':
                            
                        continp=str(input("Do you still want to continue? Y/N  ",))
                        if continp=="Y" or continp=='y':
                            cont=True
                            print()
                        elif continp=="N" or continp=='n':
                            cont=False
                        else:
                            print("please enter a valid input")
                            cont=False
            #EDITING THE BOOK PRICE
            elif et=='5':
                while contserv=="y" or contserv=="Y":
#CALLING THE MODULE
                    modules.c15.c15()
                    
                    contserv=str(input("do you want to continue this service? Y/N   ",))
                    if contserv!="Y" and contserv!="y" and contserv!="N" and contserv!='n':
                        print("error input")
                    if contserv == "N" or contserv=='n':
                            
                        continp=str(input("Do you still want to continue? Y/N  ",))
                        if continp=="Y" or continp=='y':
                            cont=True
                            print()
                        elif continp=="N" or continp=='n':
                            cont=False
                        else:
                            print("please enter a valid input")
                            cont=False
            #EDITING THE BOOK LOCATION
            elif et=='6':
                while contserv=="y" or contserv=="Y":
#CALLING THE MODULE
                    modules.c16.c16()
                    
                    contserv=str(input("do you want to continue this service? Y/N   ",))
                    if contserv!="Y" and contserv!="y" and contserv!="N" and contserv!='n':
                        print("error input")
                    if contserv == "N" or contserv=='n':
                            
                        continp=str(input("Do you still want to continue? Y/N  ",))
                        if continp=="Y" or continp=='y':
                            cont=True
                            print()
                        elif continp=="N" or continp=='n':
                            cont=False
                        else:
                            print("please enter a valid input")
                            cont=False
        #EDITING CHAPTER DATA           
        if tb=="2":
            print("""\nBook Chapter Table Menu\n
1) Chapter Title
2) Starting Page Number
3) Ending Page Number\n""")
            et=input("In which column do you need to edit data? ",)
            print()
            print("\tBooks Table\t")
            sql="select * from bookChapters"
            mycursor.execute(sql)
            rows=mycursor.fetchall()
            for row in rows:
                for col in row:
                    print('\t',col,'\t',end=' ')
                print()
            #EDITING CHAPTER TITLE
            if et=="1":
                while contserv=="y" or contserv=="Y":
#CALLING THE MODULE
                    modules.c21.c21()
                    
                    contserv=str(input("do you want to continue this service? Y/N   ",))
                    if contserv!="Y" and contserv!="y" and contserv!="N" and contserv!='n':
                        print("error input")
                    if contserv == "N" or contserv=='n':
                            
                        continp=str(input("Do you still want to continue? Y/N  ",))
                        if continp=="Y" or continp=='y':
                            cont=True
                            print()
                        elif continp=="N" or continp=='n':
                            cont=False
                        else:
                            print("please enter a valid input")
                            cont=False
            #EDITING CHAPTER STARTING PAGE NUMBER
            elif et=='2':
                while contserv=="y" or contserv=="Y":
#CALLING THE MODULE
                    modules.c22.c22()
                    
                    contserv=str(input("do you want to continue this service? Y/N   ",))
                    if contserv!="Y" and contserv!="y" and contserv!="N" and contserv!='n':
                        print("error input")
                    if contserv == "N" or contserv=='n':
                            
                        continp=str(input("Do you still want to continue? Y/N  ",))
                        if continp=="Y" or continp=='y':
                            cont=True
                            print()
                        elif continp=="N" or continp=='n':
                            cont=False
                        else:
                            print("please enter a valid input")
                            cont=False
            #EDITING CHAPTER ENDING PAGE NUMBER
            elif et=='3':
                while contserv=="y" or contserv=="Y":
#CALLING THE MODULE
                    modules.c23.c23()
                    
                    contserv=str(input("do you want to continue this service? Y/N   ",))
                    if contserv!="Y" and contserv!="y" and contserv!="N" and contserv!='n':
                        print("error input")
                    if contserv == "N" or contserv=='n':
                            
                        continp=str(input("Do you still want to continue? Y/N  ",))
                        if continp=="Y" or continp=='y':
                            cont=True
                            print()
                        elif continp=="N" or continp=='n':
                            cont=False
                        else:
                            print("please enter a valid input")
                            cont=False

                else:
                    print("please enter a valid input")
        #EDITING SUBJECT NAME
        elif tb=="3":
            while contserv=="y" or contserv=="Y":
#CALLING THE MODULE
                modules.c3.c3()
                
                contserv=str(input("do you want to continue this service? Y/N   ",))
                if contserv!="Y" and contserv!="y" and contserv!="N" and contserv!='n':
                    print("error input")
                if contserv == "N" or contserv=='n':
                        
                    continp=str(input("Do you still want to continue? Y/N  ",))
                    if continp=="Y" or continp=='y':
                        cont=True
                        print()
                    elif continp=="N" or continp=='n':
                        cont=False
                    else:
                        print("please enter a valid input")
                        cont=False
    #SEARCHING DATA
    elif x=="D" or x=="d":
        print("""\nSearch By Menu\n
1) Book Number
2) Book Title
3) Book Author
4) Book Publisher
5) Subject Code\n""")
        tb=input("What do you need to search? ",)
        print()
        #SEARCH BY BOOK NUMBER
        if tb=='1':
            while contserv=="y" or contserv=="Y":
#CALLING THE MODULE
                modules.d.d1()
                
                contserv=str(input("do you want to continue this service? Y/N   ",))
                if contserv!="Y" and contserv!="y" and contserv!="N" and contserv!='n':
                    print("error input")
                if contserv == "N" or contserv=='n':
                        
                    continp=str(input("Do you still want to continue? Y/N  ",))
                    if continp=="Y" or continp=='y':
                        cont=True
                        print()
                    elif continp=="N" or continp=='n':
                        cont=False
                    else:
                        print("please enter a valid input")
                        cont=False
        #SEACHING BY BOOK TITLE
        elif tb=='2':
            while contserv=="y" or contserv=="Y":
                #CALLING THE MODULE
                modules.d.d2()
                contserv=str(input("do you want to continue this service? Y/N   ",))
                if contserv!="Y" and contserv!="y" and contserv!="N" and contserv!='n':
                    print("error input")
                if contserv == "N" or contserv=='n':
                      
                        continp=str(input("Do you still want to continue? Y/N  ",))
                        if continp=="Y" or continp=='y':
                            cont=True
                            print()
                        elif continp=="N" or continp=='n':
                            cont=False
                        else:
                            print("please enter a valid input")
                            cont=False
            
        #SEARCHING BY BOOK AUTHOR                    
        elif tb=='3':
            while contserv=="y" or contserv=="Y":
                #CALLING THE MODULE
                modules.d.d3()
                contserv=str(input("do you want to continue this service? Y/N   ",))
                if contserv!="Y" and contserv!="y" and contserv!="N" and contserv!='n':
                    print("error input")
                if contserv == "n" or contserv=="N":
                        
                    continp=str(input("Do you still want to continue? Y/N  ",))
                    if continp=="Y" or continp=='y':
                        cont=True
                        print()
                    elif continp=="N" or continp=='n':
                        cont=False
                    else:
                        print("please enter a valid input")
                        cont=False
        #SEARCHING BY BOOK PUBLISHER
        elif tb=='4':
            while contserv=="y" or contserv=="Y":
                #CALLING THE MODULE
                modules.d.d4()

                contserv=str(input("do you want to continue this service? Y/N   ",))
                if contserv!="Y" and contserv!="y" and contserv!="N" and contserv!='n':
                    print("error input")
                if contserv == "N" or contserv == 'n':
                        
                    continp=str(input("Do you still want to continue? Y/N  ",))
                    if continp=="Y" or continp=='y':
                        cont=True
                        print()
                    elif continp=="N" or continp=='n':
                        cont=False
                    else:
                        print("please enter a valid input")
                        cont=False
        #SEARCHING BY SUBJECT CODE
        elif tb=='5':
            while contserv=="y" or contserv=="Y":
                #CALLING THE MODULE
                modules.d.d5()
                contserv=str(input("do you want to continue this service? Y/N   ",))
                if contserv!="Y" and contserv!="y" and contserv!="N" and contserv!='n':
                    print("error input")
                if contserv == "N" or contserv == 'n':                        
                    continp=str(input("Do you still want to continue? Y/N  ",))
                    if continp=="Y" or continp=='y':
                        cont=True
                        print()
                    elif continp=="N" or continp=='n':
                        cont=False
                    else:
                        print("please enter a valid input")
                        cont=False
    #READING THE BOOK CHAPTERS                  
    elif x=="E" or x=="e":
        while contserv=="y" or contserv=="Y":
#CALLING THE MODULE
                modules.e.e()
                
                contserv=str(input("do you want to continue this service? Y/N   ",))
                if contserv!="Y" and contserv!="y" and contserv!="N" and contserv!='n':
                    print("error input")
                if contserv == "N" or contserv=='n':
                        
                    continp=str(input("Do you still want to continue? Y/N  ",))
                    if continp=="Y" or continp=='y':
                        cont=True
                        print()
                    elif continp=="N" or continp=='n':
                        cont=False
                    else:
                        print("please enter a valid input")
                        cont=False
        
    #EXITING THE PROGRAM   
    elif x=="F" or x=="f":
        cont=False

    else:
        print("please enter a valid input")
        cont=False
