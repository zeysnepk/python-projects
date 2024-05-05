#guessing the number that generated from computer randomly

import random #module for generating random numbers
import time #module for waiting

play = 1


while play == 1:
    
    print("""
************************************
           WELCOME
************************************

Please guess a number 1 to 10  
          """)
    
    randomNumber = random.randint(1,10) #generates 1 to 10 random numbers

    guessCount = 3 #3 rights for guessing
    
    response = 1

    while response == 1:
        userNumber = int(input("Enter your guess: "))
    
        if userNumber < randomNumber:
        
            guessCount -= 1
            print("Comparing...")
            time.sleep(2)
            print("BİGGER")
        
        elif userNumber > randomNumber:
        
            guessCount -= 1
            print("Comparing...")
            time.sleep(2)
            print("SMALLER")
        
        else:
            
            print("CONGRATULATIONS")
            
            while True:
                
                playAgain = input("Do you want to play again(yes/no)?: ")
            
                if playAgain == "yes":
                
                    response = 0
                    break
            
                elif playAgain == "no":
                
                    response = 0
                    play = 0
                    break
                
                else:
                
                    print("Please enter a valid response")
    
    
        if guessCount == 0:
        
            print("Your right is over")
            
            while True:
                
                playAgain = input("Do you want to play again(yes/no)?: ")
            
                if playAgain == "yes":
                
                    response = 0
                    break
            
                elif playAgain == "no":

                    response = 0
                    play = 0
                    break
                
                else:
                
                    print("Please enter a valid response")
    
    


    
    