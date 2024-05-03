#Finding Fibonacci Series
numberFibo = int(input("Enter the number quantity: "))

a = 1
b = 1

fibonacci = [a,b]

for i in range(2,numberFibo):
    
    a,b = b,a+b
    fibonacci.append(b) 

print(fibonacci)


