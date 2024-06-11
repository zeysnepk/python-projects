x = set()
print(type(x))

listNums = [1,2,2,2,3,4,4,1,2,5,3,2,1]
print(set(listNums)) #takes common values just 1 time 

print(set("My name is Zeynep"))

y = {"ZEY","ZEYNEP","ZEY"} #doesnt give error but doesnt take more than 1 common value
print(y) 

#add() Function
nums = {1,2,3,4,5,6}
nums.add(7)
print(nums)

nums.add(2)
print(nums)

#difference() and difference_update() Function
set1 = {1,2,3,10,34,100,-2}
set2 = {1,2,23,34,-1}

print(set1.difference(set2))
print(set1)

print(set2.difference(set1))
print(set2)

set1.difference_update(set2)
print(set1)

set2.difference_update(set1)
print(set2)

#discard() Function
num = {1,2,3,4,5,6,7,8}
num.discard(3)
print(num)
num.discard(100)
print(num)

letters = {"A","B","C","D","E"}
letters.discard("A")
print(letters)
letters.discard("a")
print(letters)

#intersection() and intersection_update() Function
set1 = {1,2,3,10,34,100,-2}
set2 = {1,2,23,34,-1}

print(set1.intersection(set2))
print(set1)

set1.intersection_update(set2)
print(set1)

#isdisjoint() Function --> Is it a disjoint set? returns True if yes
set1 = {1,2,3,10,34,100,-2}
set2 = {1,2,23,34,-1}
set3 = {30,40,50}

print(set1.isdisjoint(set2)) #returns False because there are common values
print(set1.isdisjoint(set3)) #returns True because there are not common values it is a disjoint set

#issubset() Function --> Is it a subset? returns True if yes
set1 = {1,2,3}
set2 = {1,2,3,4}
set3 = {5,6,7}

print(set1.issubset(set2))
print(set1.issubset(set3))

#union() Function
set1 = {1,2,3,10,34,100,-2}
set2 = {1,2,23,34,-1}

print(set1.union(set2))

set1.update(set2)
print(set1)

