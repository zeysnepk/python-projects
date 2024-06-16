
list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10,11]

i = 0
values = []

while i < len(list1) and i < len(list2):
    values.append((list1[i], list2[i]))
    i += 1
    
    
print(values)


#Zip Function operates like above

print(list(zip(list1,list2)))


#Zip Function helps us to work more than 1 value at the same time with 1 for loop

nums = [1,2,3,4]
letters = ["A","B","C","D"]

for i, j in zip(nums,letters):
    print(i,j)
    
