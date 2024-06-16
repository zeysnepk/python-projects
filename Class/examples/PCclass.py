

import random
import time

WIFIpassword = "1234"
PCpassword = "12345"

class PC():
    
    def __init__(self, network_status = "OFF", bright = 50, volume = 0, apps = ["Calculator", "Recycle Bin"], files = [], folders = []):
        
        self.network_status = network_status
        self.bright = bright
        self.volume = volume
        self.apps = apps
        self.files = files
        self.folders = folders
        
    def ConnectWIFI(self):
        
        if self.network_status == "ON":
            print("Computer is already connected!")
            
        else:
            password = input("Enter the password to connect: ")
            print("Verifying Password...")
            time.sleep(1)
        
            if password == WIFIpassword:
                print("Successful Connection")
                self.network_status = "ON"
            
            else:
                print("Failed Connection")
            
    def DisconnectWIFI(self):
        
        if self.network_status == "OFF":
            print("Computer is already disconnected!")
        
        else:
            print("Disconnecting WIFI...")
            time.sleep(1)
        
            self.network_status = "OFF"
            print("Disconnected!")
            
    def BrightSettings(self):
        
        while True:
            key = input("To Increase Brightness --> '+'\nTo Decrease Brightness --> '-'\nTo Quit --> 'q'\n")

            if key == 'q':
                break
            
            elif key == '+':
                if self.bright < 100:
                    self.bright += 1
                    print("Current Bright : ",self.bright)
                    
            elif key == '-':
                if self.bright > 0:
                    self.bright -= 1
                    print("Current Bright : ",self.bright)
            
            else:
                print("Invalid Input Try Again!")
                
    def VolumeSettings(self):
        
        while True:
            key = input("To Increase Volume --> '>'\nTo Decrease Volume --> '-'\nTo Quit --> 'q'\n")

            if key == 'q':
                break
            
            elif key == '>':
                if self.volume < 100:
                    self.volume += 1
                    print("Current Volume : ",self.volume)
                    
            elif key == '<':
                if self.volume > 0:
                    self.volume -= 1
                    print("Current Volume : ",self.volume)
            
            else:
                print("Invalid Input Try Again!")
                
    def OpenApp(self):
        
        print("Apps on PC : ",self.apps)
        
        key = input("Enter the name of app you want to open: ")
        
        if key == "Calculator":
            print(
            """
            WELCOME CALCULATOR APP
            ----------------------
            
            ADDITION        --> '+'
            
            SUBTRACTION     --> '-'
            
            DIVISION        --> '/'
            
            MULTIPLICATION  --> '*'
            
            QUIT            --> 'q'
                  
            """)
            
            while True:
                op = input("Enter the operation you want to perform: ")
            
                if op == 'q':
                    break
                
                
                elif op == '+':
                    sumNums = 0
                    print("Enter the numbers you want to add until '.'")
                
                    while True:
                        point = input()
                    
                        if point == '.':
                            print("The result of addition with the given numbers = ",sumNums)
                            break
                    
                        else:
                            sumNums += float(point)
            
                elif op == '-':
                    print("Enter the numbers you want to add until '.'")
                    point = input()
                    subNums = float(point)
                
                    while point != '.':
                    
                        if point == '.':
                            print("The result of substraction with the given numbers = ",subNums)
                            break
                    
                        else:
                            point = input()
                            if point == '.':
                                print("The result of substraction with the given numbers = ",subNums)
                                break
                            else:
                                subNums -= float(point)
                        
                        
                elif op == '/':
                    print("Enter the numbers you want to add until '.'")
                    point = input()
                    divNums = float(point)
                
                    while True:
                    
                        point = input()
                        if point == '.':
                            print("The sum of the given numbers = ",divNums)
                            break
                    
                        else:
                            divNums /= float(point)
                        
                        
                elif op == '*':
                    print("Enter the numbers you want to add until '.'")
                    multiNums = 1
                
                    while True:
                        point = input()
                    
                        if point == '.':
                            print("The sum of the given numbers = ",multiNums)
                            break
                    
                        else:
                            multiNums *= float(point)
                
                else:
                    print("Invalid Input Try Again!")
                 
                        
        if key == "Recycle Bin":
            print(
            """
            WELCOME RECYCLE BIN
            -------------------
            
            DELETE FILE --> '1'
            
            DELETE FOLDER --> '2'
            
            QUIT --> 'q' 
            
            """)
            
            while True:
                key = input("Enter the selection: ")
                
                if key == 'q':
                    print("Current Files : ",self.files)
                    print("Current Folders : ",self.folders)
                    break
                
                elif key == '1':
                    print("Current Files : ",self.files)
                    
                    selectFile = input("Enter the name of file you want to delete: ")
                    
                    if selectFile in self.files:
                        self.files.remove(selectFile)
                        print("Current Files : ",self.files)
                    
                    else:
                        print("There is no ",selectFile)
                        
                elif key == '2':
                    print("Current Folders : ",self.folders)
                    
                    selectFolder = input("Enter the name of folder you want to delete: ")
                    
                    if selectFolder in self.folders:
                        self.folders.remove(selectFolder)
                        print("Current Folders : ",self.folders)
                    
                    else:
                        print("There is no ",selectFolder)
                        
                else:
                    print("Invalid Input Try Again!")
                    
    
    def AddFiles(self):
        fileName = input("Enter the name of file to add: ")
        
        print("Adding file...")
        time.sleep(1)
        self.files.append(fileName)
        print("File has been added") 
        
        print("Current Files : ",self.files)
        
    def AddFolders(self):
        folderName = input("Enter the name of folder to add: ")
        
        print("Adding folder...")
        time.sleep(1)
        self.folders.append(folderName)
        print("Folder has been added") 
        
        print("Current Folder : ",self.folder)
        
    def __str__(self):
        
        return "Network Status : {}\nBright : {}\nVolume : {}\nApps : {}\nFiles : {}\nFolders : {}\n".format(self.network_status,self.bright,self.volume,self.apps,self.files,self.folders)
        
    
PCzey = PC()
        
print(
"""
COMPUTER TURNS ON     
-----------------

***Please login to continue!***
     
""")

userpassword = input("Enter the password : ")

if userpassword == PCpassword:
    print("SUCCESSFUL LOGİN")
    
    print(
    """
            PC STATUS
    ---------------------------\n """)
    print(PCzey)
    print(
    """
    CONNECT WIFI     --> '1'
    
    DISCONNECT WIFI  --> '2'
    
    BRIGHT SETTINGS  --> '3'
    
    VOLUME SETTINGS  --> '4'
    
    OPEN AN APP      --> '5'
    
    ADD FILE         --> '6'
    
    ADD FOLDER       --> '7'
    
    PC STATUS        --> '8'
    
    QUIT             --> 'q'
    
    """)
    
    while True:
        selectionNum = input("Enter the selection: ")

        if selectionNum == 'q':
            print("COMPUTER TURNS OFF")
            break
        
        elif selectionNum == '1':
            PCzey.ConnectWIFI()
            
        elif selectionNum == '2':
            PCzey.DisconnectWIFI()
            
        elif selectionNum == '3':
            PCzey.BrightSettings()
            
        elif selectionNum == '4':
            PCzey.VolumeSettings()
            
        elif selectionNum == '5':
            PCzey.OpenApp()
            
        elif selectionNum == '6':
            PCzey.AddFiles()
        
        elif selectionNum == '7':
            PCzey.AddFolders()
        
        elif selectionNum == '8':
            print(PCzey)
            
        else:
            print("Invalid Input Try Again!")
            
    

        