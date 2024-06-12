import sqlite3

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
        

#WILL BE UPDATED
    
    

con.close()