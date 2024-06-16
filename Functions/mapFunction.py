
#Map Function maps values with a given function in tuple, list vs and returns them as a list

def double(x):
    return x * 2

map(double,[1,2,3,4,5,6,7,8])
print(map)

print(list(map(double,[1,2,3,4,5,6,7,8])))

print(list(map(lambda y  : y ** 2, (1,2,3,4,5,6,7,8,9))))


list1 = [1,2,3,4]
list2 = [1,2,3,4,5]
list3 = [1,2,3,4,5,6]

print(list(map(lambda a,b,c : a * b * c, list1, list2, list3)))


listMap = list(map(lambda a,b,c : a * b * c, list1, list2, list3))

print(listMap)




