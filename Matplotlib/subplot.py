import matplotlib.pyplot as plt
import numpy as np

x_array = np.arange(1,6)
y_array = np.arange(2,11,2)

#Plotting the first graph with x_array on the x-axis and y_array on the y-axis in red
plt.plot(x_array, y_array, "red")
plt.show() #Display the first plot

#Creating a 2x2 grid of subplots
plt.subplot(2,2,1) #First subplot (top-left)
plt.plot(x_array, y_array, "blue") #Plot with x_array and y_array in blue
plt.subplot(2,2,2)  #Second subplot (top-right)
plt.plot(y_array, x_array, "green") #Plot with y_array and x_array in green (swapped axes)
plt.subplot(2,2,3) #Third subplot (bottom-left)
plt.plot(x_array, 1 / x_array, "purple") #Plot with x_array and its reciprocal in purple
plt.subplot(2,2,4) #Fourth subplot (bottom-right)
plt.plot(x_array, y_array ** 2, "black") #Plot with x_array and the square of y_array in black

plt.show() #Display all the subplots