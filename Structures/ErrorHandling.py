#try - except is used for handling errors


#a = int("aksksks11991")  ValueError
#print(2/0)               ZeroDivisionError


try:
    a = int("aksksks11991")
except ValueError:
    print("Value of a can not be an integer")
    
try:
    print(2/0) 
except ZeroDivisionError:
    print("A number can not be division with zero")
    
    
try:
    x = int(input("Enter First Number: "))
    y = int(input("Enter Second Number: "))
    print(x/y)
except ValueError:
    print("Please enter an integer value!")
except ZeroDivisionError:
    print("Cannot divisible by 0")
print("Errors were handled!")


#FINALLY always run
try:
    z = int(input("Enter Number: "))
except ValueError:
    print("Please enter an integer value!")
finally:
    print("This section always runs")


#RAISE for throwing an error or exception
def reverseStr(name):
    if type(name) != str:
        raise ValueError("Please enter a string!")
    
    else:
        return name[::-1]

print(reverseStr("Zeynep"))
print(reverseStr(2332))

