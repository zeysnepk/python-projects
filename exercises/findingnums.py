#Finding the perfect number

num = int(input("Enter a number: "))

divisorSum = 0

for i in range(1,num):
    if num % i == 0:
        divisorSum += i
    
if divisorSum == num:
    print("Number",num,"is a perfect number")
else:
    print("Number",num,"is not a perfect number")

#Finding the armstrong number

numArm = input("Enter a number: ")
numLen = len(numArm)
numArm_sum = 0

for i in numArm:
    numArm_sum += int(i) ** numLen

if numArm_sum == int(numArm):
    print("Number",numArm,"is a Armstrong number")
else:
    print("Number",numArm,"is a not Armstrong number")


#example of list comprehension

listA = list(range(1,101))

listB = [i for i in listA if i % 2 == 0]
print(listB)

