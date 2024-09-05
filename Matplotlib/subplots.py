import matplotlib.pyplot as plt
import numpy as np

#Creating arrays for x and y values
x = np.arange(1,6)
y = np.arange(2,11,2)

#Creating a 2x2 grid of subplots and setting the figure size to 10x10 inches
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10,10))
#fig.set_size_inches(10, 10)
print(type(axes)) #Output will show that axes is a numpy array
i=1
hex_colors = ['#1f77b4', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']

#Loop through each row of subplots
for row in axes:
    for ax in row: #Loop through each subplot (ax)
        ax.plot(y, y ** i, color=hex_colors[i-1]) #Plot y raised to the power of i, colored with hex_colors
        ax.set_title(f"y = x^{i}") #Set the title of each subplot to indicate the power
        i+=1
plt.tight_layout() #Adjusts the layout to prevent overlap

#Save the figure in both PNG and PDF formats
fig.savefig("output/figure.png")
fig.savefig("output/figure.pdf")


#Create a new figure and set its size to 6x4 inches
fig_2 = plt.figure(figsize=(6,4))

#Add axes to the new figure, using the entire figure space (from 0 to 1 in both x and y directions)
axes_2 = fig_2.add_axes([0,0,1,1])

#Plot multiple functions on the same axes with different colors and labels
axes_2.plot(x, x ** 0.5, color=hex_colors[i], label="y = x^0.5")
axes_2.plot(x, x ** 2, color=hex_colors[i+1], label="y = x^2")
axes_2.plot(x, x ** 3, color=hex_colors[i+2], label="y = x^3")

#Add a legend to the second figure
axes_2.legend()

plt.show()

