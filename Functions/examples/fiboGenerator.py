#Printing fibonacci serie according to maximum number using with a generator

def fibonacci():
    
    a = 1
    b = 1
    
    yield a
    yield b
    
    while True:
        
            a, b = b, a + b
        
            yield b
    
for i in fibonacci():
    if i > 100000:
        break
    
    else:
        print(i)