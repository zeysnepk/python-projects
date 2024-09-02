import numpy as np
import pandas as pd

#Define two datasets
data_set1 = {
    "A": ["A1", "A2", "A3", "A4"],
    "B": ["B1", "B2", "B3", "B4"],
    "C": ["C1", "C2", "C3", "C4"]
}

data_set2 = {
    "A": ["A5", "A6", "A7", "A8"],
    "B": ["B5", "B6", "B7", "B8"],
    "C": ["C5", "C6", "C7", "C8"]
}

#Create DataFrames from the datasets
df1 = pd.DataFrame(data_set1, index=[1, 2, 3, 4])
df2 = pd.DataFrame(data_set2, index=[5, 6, 7, 8])


#Concatenatation
#Concatenate DataFrames along rows (default axis=0)
df3 = pd.concat([df1, df2])
print(df3)
print("----------------------------------------------------")

#Concatenate DataFrames along columns (axis=1)
df4 = pd.concat([df1, df2], axis=1)
print(df4)
print("----------------------------------------------------")


#Joining
#Create another DataFrame for joining
df3 = pd.DataFrame({"X": ["X1", "X2", "X3"], "Y": ["Y1", "Y2", "Y3"]}, index=[1, 2, 3])

#Join DataFrames (index-based join)
print(df1.join(df3))
print("----------------------------------------------------")

print(df3.join(df1))
print("----------------------------------------------------")

print(df1.join(df3, how="inner"))
print("----------------------------------------------------")

print(df1.join(df3, how="outer"))
print("----------------------------------------------------")

print(df1.join(df3, how="right"))
print("----------------------------------------------------")


#Merging
#Add a key column to both DataFrames for merging
df1["key"] = ["K1", "K2", "K5", "K4"]
df3["key"] = ["K1", "K2", "K3"]

#Merge DataFrames on the 'key' column
print(pd.merge(df1, df3, on="key"))
print("----------------------------------------------------")

print(pd.merge(df1, df3, on="key", how="outer"))
print("----------------------------------------------------")