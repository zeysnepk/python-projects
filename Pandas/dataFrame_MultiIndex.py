import numpy as np
import pandas as pd

#Create the main group by repeating each group label 3 times
main_group = np.repeat(["Group1", "Group2", "Group3"], 3)
print(main_group)
print("-----------------------------------------------")

#Create the sub group by tiling (repeating) the sequence of sub group labels 3 times
sub_group = np.tile(["Index1", "Index2", "Index3"], 3)
print(sub_group)
print("-----------------------------------------------")

#Combine main_group and sub_group into pairs using the zip function
groups = list(zip(main_group, sub_group))
print(groups)
print("-----------------------------------------------")

#Create a MultiIndex from the list of tuples created above
groups = pd.MultiIndex.from_tuples(groups)
print(groups)
print("-----------------------------------------------")

#Create a DataFrame with random numbers, using the MultiIndex for rows and three columns
df = pd.DataFrame(np.random.randn(9,3), groups, ["Column1", "Column2", "Column3"])
print(df)
print("-----------------------------------------------")

#Access the data in the "Column1" column of the DataFrame
print(df["Column1"])
print("-----------------------------------------------")

#Access all rows belonging to "Group1" (same as df.loc["Group1"])
print(df.xs("Group1"))
print("-----------------------------------------------")

#Access a specific value in "Group2", "Index1", and the "Column3" column
print(df.loc["Group2"].loc["Index1"]["Column3"]) #same with df.xs("Group2").xs("Index1").xs("Column3")
print("-----------------------------------------------")

#Add names the levels of the MultiIndex to "Groups" and "Indexes"
df.index.names = ["Groups", "Indexes"]
print(df)
print("-----------------------------------------------")

#Use the xs method to access all rows where the "Indexes" level is "Index2"
print(df.xs("Index2", level="Indexes"))

