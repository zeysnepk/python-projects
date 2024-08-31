import numpy as np

#Access the second element (index 1) in the array
arr = np.arange(1,10) 
print(arr)
print(arr[1]) #Access the second element (index 1) in the array
print(arr[2:5]) #Slice the array from index 2 to 4 (inclusive of 2, exclusive of 5)
print(arr[:4]) #Slice the array from the beginning to index 3 (inclusive of 0, exclusive of 4)
print(arr[::2]) #Slice the array with a step of 2, selecting every second element
print(arr[::-1]) #Reverse the array

#Assign the array to a new variable and modify the first three elements
arr_2 = arr
arr_2[:3] = 25
print(arr_2)
print(arr)  #arr is also modified because arr_2 is a reference to arr

#Create a copy of the array and modify all elements to 0
arr_3 = arr.copy()
arr_3[:] = 0
print(arr_3)
print(arr) #arr remains unchanged

#Create a new array and reshape it into a 5x4 matrix
new_array = np.arange(1,21).reshape(5,4)
print(new_array)

#Slice the new array to select all rows and the first two columns
new_array_2 = new_array[:,:2]
print(new_array_2)

#Slice the new array to select the first two rows and all columns
new_array_3 = new_array[:2]
print(new_array_3)

#Create an array and apply a condition to check which elements are greater than 3
arr_4 = np.arange(1,11)
print(arr_4 > 3)

#Use a boolean array to filter elements greater than 3
bool_array = arr_4 > 3
print(arr_4[bool_array])

print(arr_4[arr_4 < 5]) #Filter elements in the array that are less than 5

#Create two arrays and perform element-wise operations
arr_5 = np.array([10,20,30,40,50,60])
arr_6 = np.array([1,2,3,4,5,6])
print(arr_5 + arr_6)
print(arr_5 - arr_6)
print(arr_5 * arr_6)
print(arr_5 / arr_6)
print(arr_5 + 10)
print(arr_5 / 3)

print(np.sqrt(arr_5)) #Calculate the square root of each element in arr_5




