
#sum of the numbers with for loop
nums = [1, 6, 7, 4, 3, 8, 9, 2]
sum = 0

for val in nums:
    sum += val

print("Sum = ",sum)

#print with for loop
city = ["Ankara", "Istanbul", "Kocaeli"]
print(city)

for i in city:
    print(i)

#print letter by letter
for i in city:
    for j in range(0,len(i)):
        print(i[j])
    print("\n")

#star
starLen =int(input("Enter the lenght of triangle: "))

for i in range(starLen):
    for j in range(0,i+1):
        print("*", end = (" "))
    print("")

#twoloop
nums = ((1,2),(3,4),(5,6),(7,8))

for i,j in nums:
    print("i: {} j: {}".format(i,j))

#for in dictionaries
diction = {"one" : 1, "two" : 2, "three" : 3} 

for i in diction:
    print(i) #prints just keys

for i in diction.values():
    print(i) #prints values

for i, j in diction.items():
    print("Key : {}  Value : {}".format(i,j)) #prints keys and values


