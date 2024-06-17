from songProject import *


libsongs = libSongs()

libsongs.connectLib()

print(
"""
                    MY SONG LIST
---------------------------------------------------

'1' -----> Show All Songs
'2' -----> Show Total Song Duration
'3' -----> Add New Song
'4' -----> Delete Song
'q' -----> Quit

"""
)

while True:
    
    key = input("Enter Selection : ")
    
    if key == 'q':
        print("Exiting Program...")
        time.sleep(1)
        libsongs.disconnectLib()
        break
        
    elif key == '1':
        libsongs.showSongs()
        
    elif key == '2':
        total = libsongs.totalSongDuration()
        
        totalMinute = int(total / 60)
        totalSecond = total % 60
        
        print("Total Duration = {} minute {} second.".format(totalMinute,totalSecond))
        
    elif key == '3':
        print("Enter The Informations Of The Song You Want To Add")
        
        name = input("Name : ")
        artist = input("Artist : ")
        album = input("Album : ")
        productCompany = input("Product Company : ")
        
        durationMinute = int(input("Minute : "))
        durationSecond = int(input("Second : "))
        
        duration = (durationMinute * 60) + durationSecond
        
        songInfo = song(name,artist,album,productCompany,duration)
        
        libsongs.addSong(songInfo)
        
    elif key == '4':
        nameOfSong = input("Enter The Name Of The Song You Want To Delete : ")
        
        libsongs.deleteSong(nameOfSong)
        
    else:
        print("INVALID INPUT!")
        
        
        
        
        
