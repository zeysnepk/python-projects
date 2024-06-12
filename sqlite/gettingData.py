import sqlite3

con = sqlite3.connect("lib.db") #connecting 

cursor = con.cursor() #operations with cursor

#Getting all data from table
def gettingData():
    cursor.execute("SELECT *FROM firstable")
    listData = cursor.fetchall() #sending all data to a list with fetchall() function
    
    for i in listData:
        print(i)
    
#Getting the data with the desired content
def gettingNamesAndAuthors():
    cursor.execute("SELECT Name, Author FROM firstable") #getting just Name and Author content
    listData = cursor.fetchall()
    
    for i in listData:
        print(i)
       
#Getting the data which has the desired content 
def gettingPublisher(publisherFromUser):
    cursor.execute("SELECT *FROM firstable WHERE Publisher = ?",(publisherFromUser,)) #getting data which has publisher name received from user
    listData = cursor.fetchall()
    
    for i in listData:
        print(i)
    
gettingData()
gettingNamesAndAuthors()

publisherFromUser = input("Enter the publisher you want to search : ")
gettingPublisher(publisherFromUser)

con.close()