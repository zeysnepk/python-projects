"""
Let you have a list of pairs of numbers representing the sides of a rectangle.

         [(3,4),(10,3),(5,6),(1,9)]

Now write a function that calculates the area of a rectangle based on the side lengths and apply this function to each element of this list and print the following list on the screen.

         [12, 30, 30, 9]

*Note : try to use the map() function. 
    
"""

def area(listSights):
    return listSights[0] * listSights[1]


listSights = [(3,4),(10,3),(5,6),(1,9)]

print(list(map(area,listSights)))


