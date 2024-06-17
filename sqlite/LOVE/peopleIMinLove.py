import sqlite3
import time


class people():
    
    def __init__(self,name,surname,gender,age,score):
        
        self.name = name
        self.surname = surname
        self.gender = gender
        self.age = age
        self.score = score
        
    def __str__(self):
        
        return "\nName : {}\nSurname : {}\nGender : {}\nAge : {}\nScore : {}\n".format(self.name,self.surname,self.gender,self.age,self.score)
    

class listOfPeople():
    
    def connectLib(self):
        
        self.con = sqlite3.connect("peopleIMinLove.db")
        self.cursor = self.con.cursor()
        
        self.cursor.execute("CREATE TABLE IF NOT EXISTS listOfPeople (name TEXT, surname TEXT, gender TEXT, age INT, score FLOAT)")
        self.con.commit()
        
    def disconnectLib(self):
        
        self.con.close()
        
    def showPeople(self):
        
        self.cursor.execute("SELECT *FROM listOfPeople")
        listPeople = self.cursor.fetchall()
        
        if len(listPeople) == 0:
            print("U love nobody :(")
            
        else:
            for i in listPeople:
                People = people(i[0],i[1],i[2],i[3],i[4])
                print(People)
                
    def searchPeople(self, name):
        
        self.cursor.execute("SELECT *FROM listOfPeople WHERE name = ?",(name,))
        names = self.cursor.fetchall()
        
        if len(names) == 0:
            print("U have never been in love with",name)
            name = "nobody"
            return name
            
        else:
            peopleInfos = people(names[0][0],names[0][1],names[0][2],names[0][3],names[0][4])
            print(peopleInfos)
            
    def addPeople(self,people):
        
        self.cursor.execute("INSERT INTO listOfPeople Values(?,?,?,?,?)",(people.name,people.surname,people.gender,people.age,people.score))
        self.con.commit()
        
    def deletePeople(self,name):
        
        self.cursor.execute("DELETE FROM listOfPeople WHERE name = ?",(name,)) 
        self.con.commit()
        
    def updateAge(self,name):
        
        self.cursor.execute("SELECT *FROM listOfPeople WHERE name = ?",(name,))
        peopleList = self.cursor.fetchall()
        
        if len(peopleList) == 0:
            print("U can't update the age of someone u've never been in love with!")
            
        else:
            peopleAge = peopleList[0][3]
            peopleAge += 1
            
            self.cursor.execute("UPDATE listOfPeople SET age = ? WHERE name = ?",(peopleAge,name))
            self.con.commit()
            
    def updateScore(self,name,scoreNumber):
        
        self.cursor.execute("SELECT *FROM listOfPeople WHERE name = ?",(name,))
        peopleList = self.cursor.fetchall()
        
        if len(peopleList) == 0:
            print("U can't update the score of someone u've never been in love with!")
            
        else:
            peopleScore = peopleList[0][4]
            peopleScore += scoreNumber
            
            self.cursor.execute("UPDATE listOfPeople SET score = ? WHERE name = ?",(peopleScore,name))
            self.con.commit()
            
    