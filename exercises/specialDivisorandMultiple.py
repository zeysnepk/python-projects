#finding the greatest common divisor between two numbers

def greatestDivisor(num1,num2):
    i = 1
    divisor = 1

    while i <= num1 and i <= num2:

        if num1 % i == 0 and num2 % i == 0:
            divisor = i
        i += 1
    
    return divisor


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("The greatest common divisor between {} and {} is {}".format(num1,num2,greatestDivisor(num1,num2)))
        

#finding the smallest common multiple between two numbers

def smallestMultiple(num1,num2):
    i = 1
    multiple = 1

    while i <= num1 * num2:

        if i % num1 == 0 and i % num2 == 0:
            return i
        
        i += 1

print("The smallest common multiple between {} and {} is {}".format(num1,num2,smallestMultiple(num1,num2)))

