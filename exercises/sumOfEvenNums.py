"""
You should have a list like this.

    [1,2,3,4,5,6,7,8,9,10]

Write a function that prints the sum of the even numbers in this list to the screen.

*Note: First use filter() to remove the even numbers. Then use the reduce() function.
"""

from functools import reduce

listNums = [1,2,3,4,5,6,7,8,9,10]

listEvenNums = list(filter(lambda x : x % 2 == 0, listNums))

print(reduce(lambda x, y : x + y, listEvenNums))
