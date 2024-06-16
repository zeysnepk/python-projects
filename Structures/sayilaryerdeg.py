x = 10
y = 20

print("x = " + str(x).replace(str(x),str(y)))
print("y = " + str(y).replace(str(y),str(x)))

print("\n")

temp = x
x = y
y = temp

print("x = " + str(x))
print("y = "+str(y))

print("\n")

a = 25
b = 42

a,b = b,a

print("a = " + str(a))
print("b = " + str(b))