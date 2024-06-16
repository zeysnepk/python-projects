"""
Let you have a list where each element is a tuple of 3.

     [(3,4,5),(6,8,10),(3,10,7)]

Now write a function that returns whether these sides are a triangle or not, based on the side lengths, and print the list on the screen with only the sides indicating a triangle.

     [(3, 4, 5), (6, 8, 10)]

*** Note: Try to use the filter() function. ***
"""


def isTriangle(sights):
    if sights[0] + sights[1] > sights[2] and sights[0] + sights[2] > sights[1] and sights[1] + sights[2] > sights[0]:
        return True
    
    return False

triangleSights = [(3,4,5),(6,8,10),(3,10,7)]

print(list(filter(isTriangle, triangleSights)))


    