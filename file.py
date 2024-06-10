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

