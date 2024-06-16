#input gets str
x = input("Enter a number: ")
print(type(x))

x = x * 3 
print(x) #side by side because x is taken as a string

#to prevent it
y = int(input("Enter a number: "))
print(type(y))
y = y * 3
print(y)

#if input is not int
z = int(input("Enter a number: "))
print(z) #value error

#to prevent error
try:
    a = int(input("Enter a number: "))
    print(a)
except ValueError:
    print("Please enter a number not string")