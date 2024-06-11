#Reduce Function operates first 2 parametres and repeats the result with next parametre

from functools import reduce

def Sum(x,y):
    return x + y

print(reduce(Sum, [1,2,3,4,5]))


factorial = reduce(lambda a, b: a * b, [1,2,3,4,5])
print(factorial)


#Finding max number in given numbers

maxNum = reduce(lambda x, y : x if x > y else y, [-5,6,7,8,4,3])
print(maxNum)

#Finding min number in given numbers

minNum = reduce(lambda x, y : x if x < y else y, [-5,6,7,8,4,3])
print(minNum)