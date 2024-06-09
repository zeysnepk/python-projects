
import random
import time


class TV():
    
    def __init__(self, TV_status = "OFF", TV_sound = 0, channel_list = ["CNN"], channel = "CNN"):
        
        self.TV_status = TV_status
        self.TV_sound = TV_sound
        self.channel_list = channel_list
        self.channel = channel
        
        
    def TV_on(self):
        
        if self.TV_status == "ON":
            print("Tv is already on!\n")
        
        else:
            print("Tv turns on...\n")
            time.sleep(1)
            self.TV_status = "ON"
            
    
    def TV_off(self):
        
        if self.TV_status == "OFF":
            print("Tv is already off!\n")
        
        else:
            print("Tv turns off...\n")
            time.sleep(1)
            self.TV_status = "OFF"
            
    
    def SoundSettings(self):
                
        while True:
            
            key = input("Volume up --> '>'\nVolume down --> '<'\nQuit --> 'q'\n")

            if key == "q":
                break
            
            elif key == ">":
                if(self.TV_sound != 100):
                    self.TV_sound += 1
                    print("Volume : ",self.TV_sound)
              
            elif key == "<":
                if(self.TV_sound != 0):
                    self.TV_sound -= 1
                    print("Current Volume : ",self.TV_sound)
                
            else:
                print("Invalid input try again!")
                
    
    def AddChannel(self,channelName):
        
        print("Channel is adding...")
        time.sleep(1)
        
        self.channel_list.append(channelName)
        
        print("Channel has been added")
        
    
    def PassRandomChannel(self):
        
        randomNum = random.randint(0,len(self.channel_list)-1)
        
        self.channel = self.channel_list[randomNum]
        
        print("Current Channel : ",self.channel)
        
    
    def __len__(self):
        
        return len(self.channel_list)
    
    
    def __str__(self):
        
        return "TV Status : {}\nTV Volume : {}\nChannel List: {}\nCurrent Channel : {}\n".format(self.TV_status,self.TV_sound,self.channel_list,self.channel)
        
TVzey = TV()       
    
print(
"""
TELEVISION PROGRAM

1 --> TV ON

2 --> TV OFF

3 --> SOUND SETTING

4 --> ADD CHANNEL

5 --> NUMBER OF CHANNELS

6 --> RANDOM CHANNEL

7 --> TV INFORMATIONS

! Press 'q' to quit !
    
""")

while True:
    
    op = input("Enter the number of operation you want to do : ")
    
    if op == 'q':
        print("Exiting the Tv Program...")
        time.sleep(1)
        break
    
    elif op == '1':
        TVzey.TV_on()
        
    elif op == '2':
        TVzey.TV_off()
        
    elif op == '3':
        TVzey.SoundSettings()
        
    elif op == '4':
        channels = input("Enter the channels with ',' you want to add : ") 
        
        channelList = channels.split(',')
        
        for i in channelList:
            TVzey.AddChannel(i)
            
    elif op == '5':
        print("Number of Channels : ",len(TVzey))
        
    elif op == '6':
        TVzey.PassRandomChannel()
        
    elif op == '7':
        print(TVzey)
        
    else:
        print("Invalid Input Try Again!")
        
    
    
        
        
        
    