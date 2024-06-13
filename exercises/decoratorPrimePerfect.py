#Write a program that prints prime numbers from 1 to 1000 on the screen. Then use a decorator function to add the ability to print perfect numbers from 1 to 1000.

def perfectNums(primeNums):
    
    def wrapper(nums):
        
        perfects = list()
        
        for i in nums:
            if i == 1:
                continue
            
            else:
                totalNum = 0
            
                for j in range(1, i):
                    if i % j == 0:
                        totalNum += j
            
                if totalNum == i:
                    perfects.append(i)
                
        print("\nPERFECT NUMBERS")
        print(perfects)
        
        primeNums(nums)
        
    return wrapper

        

@perfectNums
def primeNums(nums):
    
    primes = list()
    
    for i in nums:
        
        if i == 1:
            continue
        
        elif i == 2:
            primes.append(i)
        
        else:
            isPrime = 1
            for j in range(2, i):
            
                if i % j == 0:
                    isPrime = 0
            
            if isPrime == 1:
                primes.append(i)
    
    print("\nPRIME NUMBERS")
    print(primes)
        

primeNums(range(1, 1001))
            