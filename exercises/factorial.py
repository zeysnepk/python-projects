#factorial finding program

print("""
****************************
    FACTORİAL CALCULATOR
****************************

To exit the program, press 'q'"

""")

while True:
    fac_value = input("Enter a number: ") 

    if fac_value == "q":
        print("Exiting the program...")
        break

    factorial = 1

    for i in range(2,int(fac_value)+1):
        factorial *= i

    print("Factorial of number",fac_value,"is",factorial)  
     

    

