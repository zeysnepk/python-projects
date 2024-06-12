import sqlite3
import time

con = sqlite3.connect("movies.db")

cursor = con.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS moviesIveWatched (Name TEXT, Director TEXT, Genre TEXT, Minute INT)")
con.commit()

def addAmovie():
    nameOfMovie = input("Name : ")
    directorOfMovie = input("Director : ")
    genreOfMovie = input("Genre : ")
    minuteOfMovie = int(input("Duration(minute) : "))
    
    cursor.execute("INSERT INTO moviesIveWatched Values(?,?,?,?)",(nameOfMovie,directorOfMovie,genreOfMovie,minuteOfMovie))
    con.commit()
    
def entrance():
    addAmovie()
    
    while True:
        
        key = input("\nContinue to add -----> '+'\nQuit -----> 'q'\n")
    
        if key == 'q':
            break
    
        elif key == '+':
            addAmovie()
            continue
        
        else:
            print("Please enter an valid value!")
    

def gettingALLdata():
    cursor.execute("SELECT *FROM moviesIveWatched")
    listMoviesData = cursor.fetchall()
    
    for i in listMoviesData:
        print(i)
        
def gettingMoviesInformation(infoList):
    if len(infoList) == 1:
        if infoList[0] == "name":
            cursor.execute("SELECT Name FROM moviesIveWatched",)
            listName = cursor.fetchall()
            
            for i in listName:
                print(i)
        
        elif infoList[0] == "director":
            cursor.execute("SELECT Director FROM moviesIveWatched",)
            listDirector = cursor.fetchall()
            
            for i in listDirector:
                print(i)
                
        elif infoList[0] == "genre":
            cursor.execute("SELECT Genre FROM moviesIveWatched",)
            listGenre = cursor.fetchall()
            
            for i in listGenre:
                print(i)
                
        elif infoList[0] == "minute":
            cursor.execute("SELECT Minute FROM moviesIveWatched",)
            listMinute = cursor.fetchall()
            
            for i in listMinute:
                print(i)
        
        else:
            print("INVALID INPUT")
        
    elif len(infoList) == 2:
        if "name" in infoList:
            if "genre" in infoList:
                cursor.execute("SELECT Name, Genre FROM moviesIveWatched",)
                listNameAndGenre = cursor.fetchall()
                
                for i in listNameAndGenre:
                    print(i)
                    
            elif "director" in infoList:
                cursor.execute("SELECT Name, Director FROM moviesIveWatched",)
                listNameAndDirector = cursor.fetchall()
                
                for i in listNameAndDirector:
                    print(i)
                
            elif "minute" in infoList:
                cursor.execute("SELECT Name, Minute FROM moviesIveWatched",)
                listNameAndMinute = cursor.fetchall()
                
                for i in listNameAndMinute:
                    print(i)
                
            else:
                print("INVALID INPUT")   
                    
        elif "director" in infoList:
            if "genre" in infoList:
                cursor.execute("SELECT Director, Genre FROM moviesIveWatched",)
                listDirectorAndGenre = cursor.fetchall()
                
                for i in listDirectorAndGenre:
                    print(i)
            
            elif "minute" in infoList:
                cursor.execute("SELECT Director, Minute FROM moviesIveWatched",)
                listDirectorAndMinute = cursor.fetchall()
                
                for i in listDirectorAndMinute:
                    print(i)
            
            else:
                print("INVALID INPUT")
            
        elif "genre" in infoList:
            if "minute" in infoList:
                cursor.execute("SELECT Genre, Minute FROM moviesIveWatched",)
                listGenreAndMinute = cursor.fetchall()
                
                for i in listGenreAndMinute:
                    print(i)
            
            else:
                print("INVALID INPUT")
            
        else:
            print("INVALID INPUT")
            
    elif len(infoList) == 3:
        if "name" in infoList and "director" in infoList:
            if "genre" in infoList:
                cursor.execute("SELECT Name, Director, Genre FROM moviesIveWatched",)
                listNameDirectorGenre = cursor.fetchall()
                
                for i in listNameDirectorGenre:
                    print(i)
                
            elif "minute" in infoList:
                cursor.execute("SELECT Name, Director, Minute FROM moviesIveWatched",)
                listNameDirectorMinute = cursor.fetchall()
                
                for i in listNameDirectorMinute:
                    print(i)
                    
            else:
                print("INVALID INPUT")
        
        elif "name" in infoList and "genre" in infoList and "minute" in infoList:
            cursor.execute("SELECT Name, Genre, Minute FROM moviesIveWatched",)
            listNameGenreMinute = cursor.fetchall()
                
            for i in listNameGenreMinute:
                print(i)
            
        elif "director" in infoList and "genre" in infoList and "minute" in infoList:
            cursor.execute("SELECT Director, Genre, Minute FROM moviesIveWatched",)
            listDirectorGenreMinute = cursor.fetchall()
                
            for i in listDirectorGenreMinute:
                print(i)
                
        else:
            print("INVALID INPUT")
            
    elif len(infoList) == 4:
        cursor.execute("SELECT Name, Director, Genre, Minute FROM moviesIveWatched",)
        listNameDirectorGenreMinute = cursor.fetchall()
        
        for i in listNameDirectorGenreMinute:
            print(i)
            
    else:
        print("INVALID INPUT")

    
def gettingContents(content,nameContent):
    content = content.lower()
    nameContent = nameContent.capitalize()
        
    print(nameContent)
    
    if content == "name":
        cursor.execute("SELECT *FROM moviesIveWatched WHERE Name = ?",(nameContent,))
        listContentName = cursor.fetchall()
    
        for i in listContentName:
            print(i)
            
    elif content == "director":
        cursor.execute("SELECT *FROM moviesIveWatched WHERE Director = ?",(nameContent,))
        listContentDirector = cursor.fetchall()
    
        for i in listContentDirector:
            print(i)
            
    elif content == "genre":
        cursor.execute("SELECT *FROM moviesIveWatched WHERE Genre = ?",(nameContent,))
        listContentGenre = cursor.fetchall()
    
        for i in listContentGenre:
            print(i)
            
    elif content == "minute":
        cursor.execute("SELECT *FROM moviesIveWatched WHERE Minute = ?",(nameContent,))
        listContentMinute = cursor.fetchall()
    
        for i in listContentMinute:
            print(i)
    
    
def updateMovies(content, oldName, newName):
    content = content.lower()
    
    if content == "name":
        cursor.execute("UPDATE moviesIveWatched SET Name = ? WHERE Name = ?",(newName, oldName))
        con.commit()
        
        listUpdated = cursor.execute("SELECT *FROM moviesIveWatched WHERE Name = ?",(newName,))
        
        for i in listUpdated:
            print(i)
            
    elif content == "director":
        cursor.execute("UPDATE moviesIveWatched SET Director = ? WHERE Director = ?",(newName, oldName))
        con.commit()
        
        listUpdated = cursor.execute("SELECT *FROM moviesIveWatched WHERE Director = ?",(newName,))
        
        for i in listUpdated:
            print(i)
            
    elif content == "genre":
        cursor.execute("UPDATE moviesIveWatched SET Genre = ? WHERE Genre = ?",(newName, oldName))
        con.commit()
        
        listUpdated = cursor.execute("SELECT *FROM moviesIveWatched WHERE Genre = ?",(newName,))
        
        for i in listUpdated:
            print(i)
            
    elif content == "minute":
        cursor.execute("UPDATE moviesIveWatched SET Minute = ? WHERE Minute = ?",(newName, oldName))
        con.commit()
        
        listUpdated = cursor.execute("SELECT *FROM moviesIveWatched WHERE Minute = ?",(newName,))
        
        for i in listUpdated:
            print(i)
            
    else:
        print("INVALID INPUT")
    
def deleteMovies(content, contentName):
    content = content.lower()
    
    if content == "name":
        contentList = cursor.execute("SELECT *FROM moviesIveWatched WHERE Name = ?",(contentName,))
        
        for i in contentList:
            print(i)
            
        reply = input("Are you sure to delete the above content?(Yes/No) : ")
        reply = reply.lower()
        
        if reply == "yes":
            print("DELETING CONTENT...")
            time.sleep(1)
            cursor.execute("DELETE FROM moviesIveWatched WHERE Name = ?",(contentName,))
            con.commit()
            
        elif reply == "no":
            print("GOING BACK...")
            time.sleep(1)
            
        else:
            print("INVALID INPUT")
            
    
    elif content == "director":
        contentList = cursor.execute("SELECT *FROM moviesIveWatched WHERE Director = ?",(contentName,))
        
        for i in contentList:
            print(i)
            
        reply = input("Are you sure to delete the above content?(Yes/No) : ")
        reply = reply.lower()
        
        if reply == "yes":
            print("DELETING CONTENT...")
            time.sleep(1)
            cursor.execute("DELETE FROM moviesIveWatched WHERE Director = ?",(contentName,))
            con.commit()
            
        elif reply == "no":
            print("GOING BACK...")
            time.sleep(1)
            
        else:
            print("INVALID INPUT")
            
    elif content == "genre":
        contentList = cursor.execute("SELECT *FROM moviesIveWatched WHERE Genre = ?",(contentName,))
        
        for i in contentList:
            print(i)
            
        reply = input("Are you sure to delete the above content?(Yes/No) : ")
        reply = reply.lower()
        
        if reply == "yes":
            print("DELETING CONTENT...")
            time.sleep(1)
            cursor.execute("DELETE FROM moviesIveWatched WHERE Genre = ?",(contentName,))
            con.commit()
            
        elif reply == "no":
            print("GOING BACK...")
            time.sleep(1)
            
        else:
            print("INVALID INPUT")
            
    elif content == "minute":
        contentList = cursor.execute("SELECT *FROM moviesIveWatched WHERE Minute = ?",(contentName,))
        
        for i in contentList:
            print(i)
            
        reply = input("Are you sure to delete the above content?(Yes/No) : ")
        reply = reply.lower()
        
        if reply == "yes":
            print("DELETING CONTENT...")
            time.sleep(1)
            cursor.execute("DELETE FROM moviesIveWatched WHERE Minute = ?",(contentName,))
            con.commit()
            
        elif reply == "no":
            print("GOING BACK...")
            time.sleep(1)
            
        else:
            print("INVALID INPUT")

    else:
        print("INVALID INPUT")
    
print(
"""
                        LIST OF MOVIES
    ------------------------------------------------------
"""
)

while True:
    print(""
"""
ADD MOVIE                         ----> '1'
SHOW ALL MOVIES                   ----> '2'
SHOW CERTAIN MOVIES INFORMATIONS  ----> '3'
SHOW MOVIES WITH DESIRED CONTENT  ----> '4'
UPDATE MOVIES                     ----> '5'
DELETE MOVIES                     ----> '6'
QUIT                              ----> 'q'
""")
    key = input("Select the operation : ")
    if key == 'q':
        break
    
    elif key == '1':
        entrance()
        
    elif key == '2':
        gettingALLdata()
        
    elif key == '3':
        infolist = list()
        info = input("Which informations(Name, Director, Genre, Minute) of movie you want to see?(seperate with ',') : ")
        infolist = info.split(',')
        infoListLower = [value.lower() for value in infolist]
        
        gettingMoviesInformation(infoListLower)
        
    elif key == '4':
        content = input("Which category(Name, Director, Genre, Minute)are you looking for? : ")
        contentName = input("Which content belongs movies you want to see? ")
        gettingContents(content, contentName)
        
    elif key == '5':
        content = input("Which category(Name, Director, Genre, Minute)do you want to change? : ")
        oldName = input("What is the current content name you want to change? : ")
        newName = input("What is the new content name to update? : ")
        updateMovies(content, oldName, newName)
    
    elif key == '6':
        content = input("In which category(Name, Director, Genre, Minute) is the content do you want to delete? : ")
        contentName = input("What is the content name you want to delete? : ")
        deleteMovies(content, contentName)
        
    else:
        print("INVALID INPUT")

con.close()