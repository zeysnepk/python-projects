#This section is for file operations
#!Always close file!

file = open("trial.txt","w")  #a file named "trial.txt" creates with wrtiting mode in folder where file.py is
file.write("Zeynep Kaplan")
file.close()

file2 = open("/Users/zeynepkaplan/Desktop/trial2.txt","w") #creating a file in desktop using path
file2.close()

file3 = open("trial3.txt","w",encoding = "utf-8") #utf-8 is general character format
file3.close() 

file4 = open("trial.txt","a") #opens a existing file or creates a file with append mode
file4.write(" zey\nHello\n")
file4.close()

file5 = open("trial.txt","r") #opens a existing file with reading mode
#Reading a file line by line with for 
for i in file5: 
    print(i, end = "") #to block automatically generated 1 line while reading 
file5.close()

#Reading a file with read() function
file5 = open("trial.txt","r")
readFile = file5.read()
print("\nContent of the file:\n"+readFile)

readFile2 = file5.read()
print("\nContent of the file 2:\n"+readFile2) #in previous read function went to end of the file thus current read function doesnt write anything
file5.close()

#Reading only 1 line from a file with readline() function
file6 = open("trial.txt","r")
print(file6.readline())
print(file6.readline())
print(file6.readline())
file6.close()

#Reading a file with readlines() function by putting lines into a list
file7 = open("trial.txt","r")
listFile = file7.readlines()
print(listFile)
file7.close()

#Closing files automatically "with open() as" function 
with open("trial.txt","r") as file8:
    for i in file8:
        print(i)
        
#Reading files where you want with seek() and tell() functions
with open("trial.txt","r") as file9:
    print(file9.tell())  #tells where is in the file in bytes
    file9.seek(5)        #goes to the fifth byte
    print(file9.read(6)) #reads 6 values
    

with open("trial.txt","r+") as file10:   #Opening a file with r+ mode it writes and reads
    file10.seek(3)
    file10.write("\nIs it this") #writes it starting from 3rd position
    file10.seek(0)
    print(file10.read())   
    

#Make changes at the end of the file
with open("trial.txt","r+") as file11:
    file11.read()
with open("trial.txt","a") as file11: 
    file11.write("ENDING\n")
with open("trial.txt","r+") as file11:
    print(file11.read())
    
#Make changes at the beginning of the file
with open("trial.txt","r+") as file12:
    content = file12.read()
    content = "BEGINNING\n" + content
    print(content)
    file12.seek(0)
    file12.write(content)
    file12.seek(0)
    print(file12.read())
    
#Make changes where you want in the list with lines
with open("trial.txt","r+") as file13:
    listTrial = file13.readlines()
    listTrial.insert(2,"second line\n")
    file13.seek(0)
    for i in listTrial:  #or writelines()
        file13.write(i)
    file13.seek(0)
    print(file13.read()) 
    
    