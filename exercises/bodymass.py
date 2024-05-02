print("""*********************************
BODY MASS İNDEX CALCULATOR
*********************************\n""")

weight = int(input("Enter your weight(kg): "))
height = float(input("Enter your height(m): "))

bodyMass = weight / (height ** 2)

print("Your Body Mass Index = -->",bodyMass)

if bodyMass < 18.5:
    print("***Thin***")
elif bodyMass >= 18.5 and bodyMass < 25:
    print("***Normal***")
elif bodyMass >= 25 and bodyMass < 30:
    print("***Overweight***")
else:
    print("***Obese***")
