#Printing multiples for 3 according to maximum exponent with using an Iteration

class exponent3():
    
    def __init__(self, maxNum = 0):
        
        self.maxNum = maxNum
        self.exponent = -1
        
    def __iter__(self):
         
         return self
     
    def __next__(self):
         
         self.exponent += 1
         
         if self.exponent <= self.maxNum:
             return 3 ** self.exponent
         
         else:
             self.exponent = -1
             raise StopIteration
         
for i in exponent3(5):
    print(i)
    
    
         