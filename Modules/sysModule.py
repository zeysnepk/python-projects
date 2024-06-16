
import sys

print(dir(sys))

#sys.exit()  --> exists program

sys.stderr.write("ERROR MESSAGE\n") 
sys.stderr.flush()

sys.stdout.write("message\n")

print(sys.argv)
#prints as sysargv list by writing python3 sysModule.py parameter1, parameter2, ... in terminal

#Finding roots using sys.argv in terminal
def roots(num1, num2, num3):
    
    delta = num2 ** 2 - 4 * num1 * num3
    
    if delta < 0:
        print("Reel roots do not exist!")
        
    else:
        root1 = (-num2 - delta ** 0.5) / 2 * num1
        root2 = (-num2 - delta ** 0.5) / 2 * num1
        
    return root1, root2

if len(sys.argv) == 4:
    print("FINDING ROOT\n", roots(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])))
    
else:
    sys.stderr.write("Please enter valid variables!")
    sys.stderr.flush()