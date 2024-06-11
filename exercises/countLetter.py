"""
You have a long string.

            “ProgrammingAssignmentAdvancedLevelDataStructuresandObjectsipynb”


Try to find the frequency of the letters in this string (how many times a letter occurs).
"""

array = "ProgrammingAssignmentAdvancedLevelDataStructuresandObjectsipynb"

howmanyletter = dict()

for i in array:
    if i in howmanyletter:
        howmanyletter[i] += 1
    
    else:
        howmanyletter[i] = 1
        
for i, j in howmanyletter.items():
    print(i + " ----->" , j)

