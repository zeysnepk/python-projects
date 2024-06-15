#Define a class called "Squares" and try to make this class iterable. Let the init function of this class take a parameter called maximum and print the square of the current number on the screen at every next operation. Throw the StopIteration error when you pass the maximum number.

class Squares():
    
    def __init__(self, maximum = 0):
        
        self.maximum = maximum
        self.num = 0
        
    def __iter__(self):
        
        return self
    
    def __next__(self):
        
        self.num += 1
        
        if self.num <= self.maximum:
            
            return self.num ** 2 
        
        else:
            self.num = 0
            raise StopIteration
        
squares = Squares(5)
iteration = iter(squares)

print(next(iteration))
print(next(iteration))
print(next(iteration))
print(next(iteration))
print(next(iteration))
print(next(iteration))
        
        