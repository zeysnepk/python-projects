import numpy as np

#Create a 2D array
arr = np.array([[10,20,30], [40,50,60], [70,80,90]]) 

print(arr)
print(arr[2,2]) #Accessing the element at the 3rd row, 3rd column (index starts at 0)

#Create a 1D array with values ranging from 10 to 19
arr_2 = np.arange(10,20) 

#Create a 1D array with values from 0 to 99 with a step of 3
arr_3 = np.arange(0,100,3) #set the array range triangle

#Create a 1D array consisting of ten zeros
arr_4 = np.zeros(10) #an array consisting of zeros 

#Create a 1D array consisting of ten ones
arr_5 = np.ones(10) #an array consisting of ones

#Create a 2D array of zeros with shape (3,4)
arr_6 = np.zeros((3,4)) 

#Create a 2D array of ones with shape (2,5)
arr_7 = np.ones((2,5))

#Create a 1D array of 5 evenly spaced numbers between 0 and 100
arr_8 = np.linspace(0,100,5)

#Create a 1D array of 10 random integers between 1 and 99
arr_9 = np.random.randint(1,100,10)

#Create a 2D array with a normal distribution of random numbers with shape (5,5)
arr_10 = np.random.randn(5,5)

#Create a 1D array of 10 random choices from the list [1,2,3,4,5]
arr_11 = np.random.choice([1,2,3,4,5], size=10)

#Create a 2D diagonal array
arr_12 = np.diag([1,2,3])

#Create an identity matrix of size 3x3
arr_13 = np.eye(3)

#Create a 2D array filled with the number 5
arr_14 = np.full((3,3), 5)

#Create a 2D upper triangular matrix
arr_15 = np.triu([[1,2,3],[4,5,6],[7,8,9]])

#Create a 2D lower triangular matrix, excluding the diagonal
arr_16 = np.tril([[1,2,3],[4,5,6],[7,8,9]], -1)

#Create a 2x5 array and reshape it
arr_17 = np.arange(10).reshape(2,5)

#Array statistics and manipulations
print(arr_17.min()) #Minimum value
print(arr_17.max()) #Maximum value
print(arr_17.mean()) #Mean value
print(arr_17.std()) #Standard deviation
print(arr_17.sum()) #Sum of all elements
print(arr_17.cumsum(axis=0)) #Cumulative sum along rows
print(arr_17.cumprod(axis=1))  #Cumulative product along columns
print(arr_17.argmax(axis=0)) #Index of maximum value along rows
print(arr_17.argmin(axis=0)) #Index of minimum value along rows
print(arr_17.flatten()) #Flatten the array into 1D

#Determinant of a 5x5 matrix
det_array = np.random.randint(0,100,25)
det_array = det_array.reshape(5,5)
print(det_array)

print(np.linalg.det(det_array))

#Inverse of a 5x5 matrix
inv_array = np.random.randint(0,100,25)
inv_array = inv_array.reshape(5,5)
print(inv_array)

print(np.linalg.inv(inv_array))

#Concatenation of arrays
arr_18 = np.random.randint(1,10,10).reshape(2,5) 

arr_19 = np.concatenate((arr_17, arr_18), axis=1) #Concatenate along columns

arr_20 = np.hstack((arr_17, arr_18)) #Horizontal stack (similar to concatenate along axis=1)

arr_21 = np.vstack((arr_17, arr_18)) #Vertical stack

#Repeat and tile operations
arr_22 = np.repeat(arr_17, 3, axis=0) #Repeat elements along rows

arr_23 = np.repeat(arr_17, 3, axis=1)  #Repeat elements along columns

arr_24 = np.tile(arr_17, (2,1)) #Tile the array by repeating it

#Flip operations
arr_25 = np.flip(arr_17, axis=0) #Flip array vertically

arr_26 = np.flip(arr_17, axis=1) #Flip array horizontally

#Roll operations
arr_27 = np.roll(arr_17, 1, axis=0) #Roll array elements along rows

arr_28 = np.roll(arr_17, 1, axis=1) #Roll array elements along columns
