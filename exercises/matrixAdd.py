#program for summing two given matrices

rowMatrix = int(input("Enter the matrix row: "))
colMatrix = int(input("Enter the matrix column: "))

matrix1 = [[int(input("First Matrix[{}][{}] = ".format(i,j))) for i in range(colMatrix)] for j in range(rowMatrix)]

matrix2 = [[int(input("Second Matrix[{}][{}] = ".format(i,j))) for i in range(colMatrix)] for j in range(rowMatrix)]

matrix3 = [[0] * colMatrix for i in range(rowMatrix)]
for i in range(rowMatrix):
    for j in range(colMatrix):
        matrix3[i][j] = matrix1[i][j] + matrix2[i][j]

print("-----Fist Matrix-----")
for i in range(rowMatrix):
    for j in range(colMatrix):
        print(matrix1[i][j],end = " ")
    print("\n")

print("-----Second Matrix-----")
for i in range(rowMatrix):
    for j in range(colMatrix):
        print(matrix2[i][j],end = " ")
    print("\n")

print("-----Sum Matrix-----")
for i in range(rowMatrix):
    for j in range(colMatrix):
        print(matrix3[i][j],end = " ")
    print("\n")

