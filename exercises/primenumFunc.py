#finding the prime number or non-prime using function

def primeOrnon(num):
    if num < 2:
        return False
        
    for i in range(2,num):
        if num % i == 0:
            return False
        
    return True


while True:
    num = input("Enter a number: ")

    if num == "q":
        break

    else:
        num = int(num)

        if (primeOrnon(num)):
            print(num,"is a prime number")
        
        else:
            print(num,"is not a prime number")