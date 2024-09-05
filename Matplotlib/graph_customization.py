import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 8)

#Creating a figure with two subplots arranged side by side, setting the figure size to 12x6 inches
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# First plot with existing customizations
ax1.plot(x, x ** 2.5, color="pink", linewidth=3, linestyle="--", alpha=0.8, #Plot with pink dashed line and some transparency
         marker="o", markersize=10, markerfacecolor="yellow", #Circle markers with yellow inside
         markeredgecolor="red", markeredgewidth=3) #Red marker edges with a width of 3

#Customizing the first plot's axes limits, title, and labels
ax1.set_xlim([0, 7]) #Set x-axis limits
ax1.set_ylim([0, 150]) #Set y-axis limits
ax1.set_title("Original Plot", fontsize=16, fontweight='bold') #Set title with bold font
ax1.set_xlabel("X-axis", fontsize=12) #Label for the x-axis
ax1.set_ylabel("Y-axis", fontsize=12) #Label for the y-axis
ax1.grid(True, linestyle=':', alpha=0.7) #Add grid with dotted lines and some transparency

# Second plot with more customizations
y1 = x ** 2
y2 = x ** 1.5

#Plotting y1 and y2 with different colors and line styles
ax2.plot(x, y1, color="blue", linewidth=2, linestyle="-", label="y = x^2") #y = x^2 plot in blue with solid line
ax2.plot(x, y2, color="green", linewidth=2, linestyle="--", label="y = x^1.5") #y = x^1.5 plot in green with dashed line

#Filling the area between y1 and y2 where y1 > y2 with blue, and where y1 <= y2 with green
ax2.fill_between(x, y1, y2, where=(y1 > y2), alpha=0.3, color='skyblue')
ax2.fill_between(x, y1, y2, where=(y1 <= y2), alpha=0.3, color='lightgreen')

#Customizing the second plot's axes limits, title, and labels
ax2.set_xlim([0, 7])
ax2.set_ylim([0, 50])
ax2.set_title("Additional Customizations", fontsize=16, fontweight='bold')
ax2.set_xlabel("X-axis", fontsize=12)
ax2.set_ylabel("Y-axis", fontsize=12)

#Adding a legend in the upper left corner
ax2.legend(loc='upper left', fontsize=10)

#Adding grid lines with a different style and transparency
ax2.grid(True, linestyle='--', alpha=0.5)

#Customize tick labels
ax2.tick_params(axis='x', which='major', labelsize=12, colors='red')
ax2.tick_params(axis='y', which='major', labelsize=12, colors='purple')

#Adding an annotation with an arrow pointing to the intersection of the two curves
ax2.annotate('Intersection', xy=(4, 16), xytext=(5, 30),
             arrowprops=dict(facecolor='black', shrink=0.05))

#Setting the background color of the second plot to yellow
ax2.set_facecolor("yellow")

plt.tight_layout()
plt.show()