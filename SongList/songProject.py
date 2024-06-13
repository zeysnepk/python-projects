import sqlite3
import time


class song():
    
    def __init__(self,name,artist,album,productionCompany,duration):
        
        self.name = name
        self.artist = artist
        self.album = album
        self.productionCompany = productionCompany
        self.duration = duration
        
    def __str__(self):
        
        return "\nName : {}\nArtist : {}\nAlbum : {}\nProduction Company : {}\nSong Duration : {} second\n".format(self.name,self.artist,self.album,self.productionCompany,self.duration)
    
    

class libSongs():
    
    def connectLib(self):
        
        self.con = sqlite3.connect("libSongs.db")
        
        self.cursor = self.con.cursor()
        
        self.cursor.execute("CREATE TABLE IF NOT EXISTS songs(NAME TEXT, ARTIST TEXT, ALBUM TEXT, PRODUCTION COMPANY TEXT, DURATION INT)")
        
        self.con.commit()
        
    def disconnectLib(self):
        
        self.con.close()
        
    def totalSongDuration(self):
        
        self.cursor.execute("SELECT DURATION FROM songs")
        
        print("Calculating Total Duration...")
        time.sleep(2)
        
        durationList = self.cursor.fetchall()
        
        totalDuration = 0
        for i in durationList:
            print(i[0])
            totalDuration += i[0]
            
        print(totalDuration)
        return totalDuration
    
    def addSong(self,song):
        
        self.cursor.execute("SELECT *FROM songs WHERE NAME = ?",(song.name,))
        sameName = self.cursor.fetchall()
        
        self.cursor.execute("SELECT *FROM songs WHERE ARTIST = ?",(song.artist,))
        sameArtist = self.cursor.fetchall()
        
        if len(sameName) == 0 and len(sameArtist) == 0:
        
            print("Adding New Song...")
            time.sleep(1)
            
            self.cursor.execute("INSERT INTO songs VALUES(?,?,?,?,?)",(song.name,song.artist,song.album,song.productionCompany,song.duration))
            self.con.commit()
            
            print("Added New Song")
            
        else:
            print("The Song Already Exists!")
    
    def deleteSong(self,songName):
        
        print("Searching Song...")
        time.sleep(1)
        
        self.cursor.execute("SELECT *FROM songs WHERE NAME = ?",(songName,))
        sameName = self.cursor.fetchall()
        
        if len(sameName) == 0:
            print("The Song Not Exists!")
            
        else:
            print("Song Found!")
            
            for i in sameName:
                songInfo = song(i[0],i[1],[2],[3],i[4])
                
                print(songInfo)
                
                while True:
                    
                    key = input("Are You Sure?(YES/NO) : ")
                
                    if key.lower() == "yes":
                        print("Deleting Song...")
                        time.sleep(2)
                    
                        self.cursor.execute("DELETE FROM songs WHERE NAME = ?",(songName,))
                        self.con.commit()
                    
                        print("Deleted Song!")
                    
                    elif key.lower() == "no":
                        print("Going Back...")
                        time.sleep(1)
                        break
                    
                    else:
                        print("INVALID INPUT!")  
                        
    def showSongs(self):
        
        print("Searching All Songs...")
        time.sleep(2)
        
        self.cursor.execute("SELECT *FROM songs")
        
        allSongs = self.cursor.fetchall()
        
        if len(allSongs) == 0:
            print("There is no song!")
            
        else:
            for i in allSongs:
                songInfos = song(i[0],i[1],i[2],i[3],i[4])
                print(songInfos)
            
            
        
        
        