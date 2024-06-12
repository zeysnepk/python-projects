from peopleIMinLove import *

print(
"""
            LIST OF PEOPLE I'M IN LOVE WITH
------------------------------------------------------------

'1' -----> SHOW PEOPLE INFORMATIONS
'2' -----> ADD NEW PEOPLE 
'3' -----> DELETE PEOPLE 
'4' -----> SEARCH PEOPLE
'5' -----> UPDATE AGE OF PEOPLE
'6' -----> UPDATE SCORE OF PEOPLE
'q' -----> QUIT 

"""
)

listPeople = listOfPeople()
listPeople.connectLib()

while True:
    key = input("Enter your selection : ")
    
    if key == 'q':
        print("Exiting Program...")
        time.sleep(1)
        break

    elif key == '1':
        print("Receiving Data..")
        time.sleep(1)
        
        listPeople.showPeople()
        
    elif key == '2':
        print("Enter the informations of person u want to add")
        name = input("Name : ")
        surname = input("Surname : ")
        
        while True:
            gender = input("Gender(man/woman) : ")
            gender = gender.lower()
            
            if gender == "man" or gender == "woman":
                break
            
            else:
                print("Enter 'man' or 'woman'!")
                continue
        
        age = int(input("Age : "))
        score = float(input("Score : "))
        
        newPeople = people(name,surname,gender,age,score)
        
        print("Adding People...")
        time.sleep(1)
        
        listPeople.addPeople(newPeople)
        
        print("Person Added Successfully")
        
    elif key == '3':
        nameToDelete = input("Enter the name of person u want to delete : ")
        
        nameToDelete = listPeople.searchPeople(nameToDelete)
        
        if nameToDelete != "nobody":
            
            while True:
                yesOrNo = input("Are You Sure?(Yes/No) : ")
                yesOrNo = yesOrNo.lower()
        
                if yesOrNo == "yes":
                    print("Deleting",nameToDelete,"from your heart and list...")
                    time.sleep(1)
            
                    listPeople.deletePeople(nameToDelete)
            
                    print("Deleted :(")
                    break
        
                elif yesOrNo == "no":
                    print("I knew it was a tough decision :)")
                    break
            
                else:
                    print("INVALID INPUT TRY AGAIN!")
            
    elif key == '4':
        nameToSearch = input("Which person are u looking for? : ")
        
        print("Searching",nameToSearch,"...")
        time.sleep(1)
        
        listPeople.searchPeople(nameToSearch)
    
    elif key == '5':
        nameToUpdate = input("Who grew up? : ")
        
        print("Searching",nameToUpdate,"...")
        time.sleep(1)
        
        listPeople.updateAge(nameToUpdate)
        
    elif key == '6':
        nameToUpdate = input("Which person's score u want to change? : ")
        scoreNumber = float(input("Enter score increase(+) or decrease(-) : "))
        print(scoreNumber)
        
        print("Searching",nameToUpdate,"...")
        time.sleep(1)
        
        listPeople.updateScore(nameToUpdate,scoreNumber)  
    
    else:
        print("INVALID INPUT")
        
listPeople.disconnectLib()
        
        
        
    