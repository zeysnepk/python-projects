#Sending desired number of parameters to a function
def send(*args):
    
    for i in args:
        print(i)
        
send(1,2,3,4,5,6)
send(10,100)


#Sending parameters to form a dictionary
def sendict(**kwargs):
    print(kwargs)
    
    for i, j in kwargs.items():
        print(i," : ",j)
    
sendict(Name = "Zeynep", no = 123)


#Defining functions as variables
def sumNums(x, y):
    print(x + y)
    
sumNums(4, 6)

sumNumsCopy = sumNums 

sumNumsCopy(2, 8)

del sumNums  #sumNums(4, 6) #gives an error for deletion

sumNumsCopy(2, 6) #Usable even if sumNums deleted


#Nested Functions
def func1():
    
    def func2():
        print("Executed second function!")
    
    func2()
    print("Executed First Function!")
    
func1() #to execute func2() gives NameError

def funcAgrs(*args):
    
    def sumArgs(args):
        
        sumNums = 0
        for i in args:
            sumNums += i
        
        return sumNums
    print(sumArgs(args))
    
funcAgrs(1,2,3,4,5,6,7)


#Returning Nested Functions
def main(op):
    
    def additionMain(*args):
        sumNums = 0
        
        for i in args:
            sumNums += i
        
        return sumNums
    
    def multiplicationMain(*args):
        multiNums = 1
    
        for i in args:
            multiNums *= i
            
        return multiNums
    
    def nothingMain(*args):
        return 0
    
    if op == '+':
        return additionMain
    
    elif op == '*':
        return multiplicationMain
    
    else:
        return nothingMain
    
sumFunc = main('+')
multiFunc = main('*')
noFunc = main('-')

print(sumFunc(1,2,3,4,5))
print(multiFunc(1,2,3,4,5))
print(noFunc(1,2,3,4,5))


def addition(num1, num2):
    return num1 + num2

def multiplication(num1, num2):
    return num1 * num2

def subtraction(num1, num2):
    return num1 - num2

def division(num1, num2):
    return num1 / num2

def mainFunction(func1, func2, func3, func4, op, x, y):
    
    if op == '+':
        print(func1(x, y))
        
    elif op == '*':
        print(func2(x, y))
        
    elif op == '-':
        print(func3(x, y))
        
    elif op == '/':
        print(func4(x, y))
        
    else:
        print("INVALID INPUT")
        
key = input("Enter the operation(+, *, -, /) : ")

n1 = int(input("Enter first number : "))
n2 = int(input("Enter second number : "))

print(mainFunction(addition, multiplication, subtraction, division, key, n1, n2))

        
    