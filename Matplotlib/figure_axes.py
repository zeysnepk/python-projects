import matplotlib.pyplot as plt
import numpy as np

#Creating arrays for x and y values
x = np.arange(1,6)
y = np.arange(2,11,2)

#Creating a figure
fig = plt.figure()

#Adding first set of axes (top-left small subplot)
axes1 = fig.add_axes([0.1, 0.6, 0.2, 0.35])

#Adding second set of axes (bottom-left small subplot)
axes2 = fig.add_axes([0.1, 0.1, 0.2, 0.35])

#Adding third set of axes (large outer graph on the right)
axes3 = fig.add_axes([0.5, 0.1, 0.4, 0.8])

#Adding fourth set of axes (inner graph within the large one)
axes4 = fig.add_axes([0.6, 0.3, 0.2, 0.4])

#Plotting on the large outer graph
axes3.plot(x,y)
axes3.set_xlabel("OUTER X")
axes3.set_ylabel("OUTER Y")
axes3.set_title("OUTER GRAPH")

#Plotting on the inner inset graph
axes4.plot(x,y)
axes4.set_xlabel("INNER X")
axes4.set_ylabel("INNER Y")
axes4.set_title("INNER GRAPH")

#Display the plot
plt.show()