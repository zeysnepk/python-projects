
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



