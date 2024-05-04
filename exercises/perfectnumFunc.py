#finding the perfect numbers from 1 to 1000

def perfectNum(num):
    sumofdivisors = 0

    for i in range(1,num):
        if num % i == 0:
            sumofdivisors += i

    return sumofdivisors

print("PERFECT NUMBERS")

for i in range(1,1001):
    sumNums = perfectNum(i)

    if sumNums == i:
        print(i)



