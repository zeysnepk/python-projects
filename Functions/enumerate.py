listColors = ["Yellow","Green","Red","Brown"]
i = 0
colorsNumbers = []

while(i < len(listColors)):
    colorsNumbers.append((i,listColors[i]))
    i += 1
    
print(colorsNumbers)


#Enumerate Function works like above
print(list(enumerate(listColors)))

for i, j in enumerate(listColors):
    print(i,j)
    

#Printing values has even index with enumerate function

listLetters = ["a","b","c","d","e","f","g","h"]

for i, j in enumerate(listLetters):
    if i % 2 == 0:
        print(j)
        
