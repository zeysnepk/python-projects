import sqlite3

con = sqlite3.connect("lib.db") #Connecting table

cursor = con.cursor() #A cursor to operate on database

#Creating a table 
cursor.execute("CREATE TABLE IF NOT EXISTS firstable (Name TEXT, Author TEXT, Publisher TEXT, NumbersofPages INT)")
con.commit() #commit() is required to be valid on database

#Adding data to table
cursor.execute("INSERT OR IGNORE INTO firstable VALUES('Crime and Punishment','Dostoevsky','The Russian Messenger',527)") #executing
con.commit()

#Adding data to table from user
nameOfBook = input("Name : ")
authotOfBook = input("Author : ")
publisherOfBook = input("Publisher : ")
numbersOfBookspage = int(input("Numbers of Pages : "))

cursor.execute("INSERT INTO firstable Values(?,?,?,?)",(nameOfBook,authotOfBook,publisherOfBook,numbersOfBookspage))
con.commit()


con.close()