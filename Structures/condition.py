
#Comparison
x = input("enter first number: ")
y = input("enter second number: ")


if x == y:
    print("The numbers are equal")

elif x > y:
    print("The number",x,"is greater than number",y)

else:
    print("The number",y,"is greater than number",x)


#Positive or Negative or Neutral
num = int(input("enter a number: "))

if num == 0:
    print("The number",num,"is neutral")

elif num > 0:
    print("The number",num,"is positive")

else:
    print("The number",num,"is negative")


#Finding max and min nums
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a>b and a>c:
    maxNum = a
    if b>c:
        minNum = c
    else:
        minNum = b
elif b>c:
    maxNum = b
    if a>c:
        minNum = c
    else:
        minNum = a
else:
    maxNum = c
    if a>b:
        minNum = b
    else:
        minNum = a

print("\nThe biggest number is",maxNum,"\nThe smallest number is",minNum)

#bool
bool(0) #False
bool(1) #True
bool(13) #True 
