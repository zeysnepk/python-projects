import numpy as np
import pandas as pd

#Create a dataset with product, region, sales, and quantity information
data_set = {
    "Product": ["Laptop ", "Smartphone ", "Tablet ", "Monitor ", "Keyboard ", "Headphones "],
    "Region": ["North", "South", "East", "West", "North", "South"],
    "Sales": [1500, 800, 400, 600, 200, 150],
    "Quantity": [10, 25, 15, 12, 40, 30]
}

#Convert the dataset into a DataFrame
df = pd.DataFrame(data_set)
print(df)
print("----------------------------------------------------------")

#Group the DataFrame by the 'Region' column
group_region = df.groupby('Region')
#Sum the numerical columns for each region and display the result
print(group_region.sum())
print("----------------------------------------------------------")

#Display the sum of numerical columns specifically for the 'North' region
print(group_region.sum().loc['North'])
print("----------------------------------------------------------")

#Display the sum of the 'Sales' column specifically for the 'North' region
print(group_region.sum().loc['North'].loc['Sales'])
print("----------------------------------------------------------")

#Count the number of non-NaN values in each column for each region
print(group_region.count())
print("----------------------------------------------------------")

#Find the maximum values for each numerical column by region
print(group_region.max())
print("----------------------------------------------------------")

#Find the minimum values for each numerical column by region
print(group_region.min())
print("----------------------------------------------------------")

#Find the minimum values of the 'Sales' column by region
print(group_region.min()['Sales'])
print("----------------------------------------------------------")

#Find the minimum 'Sales' value specifically for the 'West' region
print(group_region.min()['Sales']['West'])
print("----------------------------------------------------------")