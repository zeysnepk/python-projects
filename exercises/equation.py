#finding the roots of a quadratic equation --> ax^2 +bx + c

#getting the numbers from user (a,b,c)
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

#calculating delta
delta = b ** 2 - 4 * a * c

#calculating the roots
root1 = (-b - delta ** 0.5) / (2 * a)
root2 = (-b + delta ** 0.5) / (2 * a)

#printing the roots
if delta > 0:
    print("The roots of the equation are {} and {}".format(root1,root2))
elif delta == 0:
    print("The roots are equal and values {}".format(root1))
else:
    print("There is no solution in real numbers")


