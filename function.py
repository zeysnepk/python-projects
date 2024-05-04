#factorial with function

def fac_calculator(fac_value):
    factorial = 1

    for i in range(2, fac_value+1):
        factorial *= i

    print("Factorial of the number",fac_value,"is",factorial)

fac_valueint = int(input("Enter a number: "))
fac_calculator(fac_valueint)


#factorial with return function

def fac_calculator(fac_value):
    factorial = 1

    for i in range(2, fac_value+1):
        factorial *= i

    return factorial

fac_valueint = int(input("Enter a number: "))
fac_result = fac_calculator(fac_valueint)

print(fac_result)

#nested function

def multiplyThree(num):
    print("multiplied by three")
    return num * 3

def addTwo(num):
    print("added two")
    return num + 2

def divideFour(num):
    print("divided into four")
    return num / 4

num = int(input("Enter a number: "))
print(divideFour(addTwo(multiplyThree(num))))

#default value in a function

def printName(name = "Anonymous"):
    print("Name:",name)

printName() #no parameter is given so prints default 
printName("Zeynep")


#flexible parameters

def sum(*nums):
    sumNums = 0
    for i in nums:
        sumNums += i
    return sumNums

print(sum(1,2,3,4,5,6,7,8,9))


#global and local variables

c = 10 #global variable

def func(): # c has both global and local value
    c = 2 #local variable
    print(c) #prints local variable

func()
print(c) #prints global variable


#to use global variable in function

b = 10

def functionGlobal():
    global b
    b = 2
    print(b)

functionGlobal()
print(b)


#Lambda Function

multipTwo = lambda x : x *2 #creates a function on a single line
print(multipTwo(5)) 

reverse = lambda s : s[::-1] #reverses string
print(reverse("Zeynep"))