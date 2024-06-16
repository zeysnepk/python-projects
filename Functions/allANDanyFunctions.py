
def isTrue(listBools):
    for i in listBools:
        if not i:
            return False
        
    return True

listBools = [True,False,False,True,True]
print(isTrue(listBools))

#All Function works like above which means if all of values are True returns True otherwise returns False
print(all(listBools))


def isFalse(listBools):
    for i in listBools:
        if i:
            return True
        
    return False

print(isFalse(listBools))

#Any Function works like above which means if all of values are False returns False otherwise returns True
print(any(listBools))


