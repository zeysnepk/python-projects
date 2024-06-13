
import time

#Decorator Function is used to avoid rewriting as the following comment lines

def calculateTime(function):
    
    def wrapper(nums):
        
        startingTime = time.time()
        
        result = function(nums)
        
        endingTime = time.time()
    
        print(function.__name__, "lasted", endingTime - startingTime, "second.\n")    
        return result
    return wrapper

@calculateTime
def calculateSquare(nums):
    
    res = list()
    
    #startingTime = time.time()
    
    for i in nums:
        res.append(i ** 2)
        
    #endingTime = time.time()
    #print("Square Calculation lasted", endingTime - startingTime, "second.\n")  
    
    return res

@calculateTime
def calculateCube(nums):
    
    res = list()
    
    #startingTime = time.time()
    
    for i in nums:
        res.append(i ** 3)
        
    #endingTime = time.time()
    #print("Square Calculation lasted", endingTime - startingTime, "second.\n")  
    
    return res

print(calculateSquare(range(10)))
print("\n\n")
print(calculateCube(range(10)))

