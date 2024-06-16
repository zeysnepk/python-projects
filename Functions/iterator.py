#Provides to return each elemenet in order for thypes with more than one element such as list, tuple, strings vs

listNums = [1,2,3,4,5]

iteratorCreate = iter(listNums) #creating an iteration object with iter() function

print(iteratorCreate) 

print(next(iteratorCreate)) #printing elements in order
print(next(iteratorCreate))
print(next(iteratorCreate))
print(next(iteratorCreate))
print(next(iteratorCreate))
#print(next(iteratorCreate)) gives StopIteration error cuz next element does not exist

print("\n\n")

#Iterations are used in for loops
listNum = [1,2,3,4,5,6,7,8,9,10]
print("Elements with for loop")

for i in listNums:
    print(i)

#for loop above works in itself as follows
print("\nElements with iteration")
iterator = iter(listNums)

while True:
    try:
        print(next(iterator))
    except StopIteration:
        break
    
print("\n\n")

#Defining Iteration with using a Class
class Channels():
    def __init__(self,channelList):
        self.channelList = channelList
        self.index = -1
        
    def __iter__(self):
        return self
    
    def __next__(self):
        self.index += 1
        
        if self.index < len(self.channelList):
            return self.channelList[self.index]

        else:
            self.index = -1
            raise StopIteration
        
channels = Channels(["CNN","BBC News","Fox","HBO","National Geographic"])
iteration = iter(channels)

print("-------CHANNELS-------")
print(next(iteration))
print(next(iteration))
print(next(iteration))
print(next(iteration))
print(next(iteration))
#print(next(iteration)) StopIteration Error

channels = Channels(["CNN","BBC News","Fox","HBO","National Geographic"])
print("\n\n")
for i in channels:
    print(i)