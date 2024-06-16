#Generators is generally used for creating iteration objects and do not take space in memory

#A function without using generator
def takeSquare():
    
    listNums = []
    
    for i in range(1,10):
        listNums.append(i ** 2)
        
    return listNums

print(takeSquare())

#If working in a larger number range, using generators is more memory efficient

#The yield key word is used for generators
def takeCube():
    
    for i in range(1,10):
        yield i ** 3
        
iterator = iter(takeCube())
print(next(iterator))
print(next(iterator))
print(next(iterator))

#{} is used instead of [] to convert List Comprehension to Generator Object 
listNum = [i * 2 for i in range(1,10)] #List Comprehension
print(listNum)

generator = {i * 2 for i in range(1,10)}
iteration = iter(generator)

print(next(iteration))
print(next(iteration))
print(next(iteration))
print(next(iteration))


#Multiplication Table with using a generator
print("\n\n-----MULTIPLICATION TABLE-----\n")
def table():
    
    for i in range(1,6):
        for j in range(1,6):
            yield "{} x {} = {}".format(i,j,i * j)
            
for i in table():
    print(i)

        
