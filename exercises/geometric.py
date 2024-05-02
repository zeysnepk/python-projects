# geometric shape calculation

print("""********************************************
\tGEOMETRİC SHAPE CALCULATION
********************************************""")

shape = input("Triangle or Quadrilateral: ")


if shape.lower() == "quadrilateral":
    print("Enter the sights of quadrilateral: ")
    q1 = float(input())
    q2 = float(input())
    q3 = float(input())
    q4 = float(input())

    if q1 == q2 == q3 == q4:
        print("Square")
    elif q1 == q2 and q3 == q4 or q1 == q3 and q2 == q4 or q1 == q4 and q2 == q3:
        print("Rectangle") 
    else:
        print("Ordinary Quadrilateral")
    
elif shape.lower() == "triangle":
    print("Enter the sights of triangle: ")
    t1 = float(input())
    t2 = float(input())
    t3 = float(input())

    if t1 < t2 + t3 and t1 > abs(t2 - t3) and t2 < t1 + t3 and t2 > abs(t1 - t3) and t3 < t2 + t1 and t3 > abs(t2 - t1):
        if t1 == t2 == t3:
            print("Equilateral Triangle")
        elif t1 == t2 or t1 == t3 or t2 == t3:
            print("Isosceles Triangle")
        elif t1 < t2 + t3 and t1 > abs(t2 - t3) and t2 < t1 + t3 and t2 > abs(t1 - t3) and t3 < t2 + t1 and t3 > abs(t2 - t1):
            print("Ordinary Triangle")
    else:
        print("Triangle does not specify")