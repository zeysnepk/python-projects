#Write a generator function that generates prime numbers from numbers from 1 to 1000.

def primeGenerator():
    
    
    
    num = 2
    yield 2
    
    while True:
        boolNum = 1
        num += 1
        for i in range(2, int(num/2)):
            if num % i == 0:
                boolNum = 0
                    
        if boolNum == 1:
            yield num

for i in primeGenerator():
    if i > 1000:
        break
    print(i)