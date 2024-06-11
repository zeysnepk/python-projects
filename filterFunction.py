#Filter Function returns values which are True 

#Finding even numbers with Filter Function
evenNums = list(filter(lambda x: x % 2 == 0, [1,2,3,4,5,6,7,8,9,10]))

print(evenNums)

#Finding prime numbers 

def primeNums(y):
    
    if y == 1:
        return False
    
    elif y == 2:
        return True
    
    else:
        i = 2
        
        while(i < y):
            
            if y % i == 0:
                return False
            
            i += 1
        
        return True
    

print(list(filter(primeNums, range(1,100))))