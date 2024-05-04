#finding the exact divisors of numbers using function

divisorsList = []

def exactDivisors(num):
    for i in range(1,num+1):
        if num % i == 0:
            divisorsList.append(i)



while True:
    num = input("Enter a number: ")

    if num == "q":
        break

    else:
        num = int(num)

        exactDivisors(num)
        print("The exact divisors of",num," :",divisorsList)

    


