import sqlite3

con = sqlite3.connect("lib.db")

cursor = con.cursor()

#Updating Data
def updateData(oldPublisher, newPublisher):
    cursor.execute("UPDATE firstable SET Publisher = ? WHERE Publisher = ?",(newPublisher,oldPublisher))
    con.commit()
    
updateData("The Russian Messenger", "The Russian Artist")

#Deleting Data
def deletingData(AuthorForDelete):
    cursor.execute("DELETE FROM firstable WHERE Author = ?",(AuthorForDelete,))
    con.commit()
    
deletingData("Jojo Moyes")
con.close()