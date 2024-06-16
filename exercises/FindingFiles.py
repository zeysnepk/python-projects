#Search for all mp4, txt and pdf files on your computer with the os module and save their location and names in separate files named "pdf_files.txt", "mp4_files.txt", "txt_files.txt".

import os
import sys

print(dir(os))

os.chdir("/Users/zeynepkaplan/Desktop/PythonProjects/exercises")
print(os.getcwd())

txtDict = dict()
mp4Dict = dict()
pdfDict = dict()

for file in os.walk("/Users/zeynepkaplan/Desktop"):
    for fileName in file:
        for fileFind in fileName:
            if fileFind.endswith(".txt"):
                txtDict[fileFind] = file[0]
            
            if fileFind.endswith(".mp4"):
                mp4Dict[fileFind] = file[0]
                
            if fileFind.endswith(".pdf"):
                pdfDict[fileFind] = file[0]
            
                
            

for name, path in txtDict.items():
    print("TXT name : {}\nTXT path : {}\n".format(name,path))
    
print("********************************************************************")
    
for name, path in mp4Dict.items():
    print("MP4 name : {}\nMP4 path : {}\n".format(name,path))
    
print("********************************************************************")

for name, path in pdfDict.items():
    print("PDF name : {}\nPDF path : {}\n".format(name,path))
    

with open ("pdf_files.txt","w") as file:
    
    for name, path in pdfDict.items():
        file.write("PDF name : {}\nPDF path : {}\n\n".format(name,path))
    
    file.close()
    

with open ("txt_files.txt","w") as file:
    
    for name, path in txtDict.items():
        file.write("TXT name : {}\nTXT path : {}\n\n".format(name,path))
    
    file.close()     

with open ("mp4_files.txt","w") as file:
    
    for name, path in mp4Dict.items():
        file.write("MP4 name : {}\nMP4 path : {}\n\n".format(name,path))
    
    file.close()
        
