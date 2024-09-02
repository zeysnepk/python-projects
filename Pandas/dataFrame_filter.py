import numpy as np
import pandas as pd

#Create a DataFrame with random numbers, indexed by 1 to 5 and columns labeled A, B, C
df = pd.DataFrame(np.random.randn(5,3), [1, 2, 3, 4, 5], ["A", "B", "C"])

#Create a boolean DataFrame where each value is True if it's greater than 0, otherwise False
df_bool = df > 0
print(df_bool)
print("-------------------------------------")

#Use the boolean DataFrame to filter the original DataFrame, keeping only values greater than 0
print(df[df_bool]) #same with df[df > 0]
print("-------------------------------------")

#Check which values in column "A" are greater than 0
print(df["A"] > 0)
print("-------------------------------------")

#Filter the DataFrame to keep only rows where the values in column "A" are greater than 0
print(df[df["A"] > 0])
print("-------------------------------------")

#Filter the DataFrame to keep only rows where the values in column "B" are greater than 0
print(df[df["B"] > 0])
print("-------------------------------------")

#Filter the DataFrame to keep only rows where values in both columns "A" and "B" are greater than 0
print(df[(df["A"] > 0) & (df["B"] > 0)])
print("-------------------------------------")


#Filter the DataFrame to keep rows where either column "A" or "B" has values greater than 0
print(df[(df["A"] > 0) | (df["B"] > 0)])
print("-------------------------------------")

#Add a new column "D" with random values, using np.random.randn(5)
df["D"] = np.random.randn(5) #same with dp.Series(np.random.rand(5))
print(df)
print("-------------------------------------")

#Set column "D" as the new index of the DataFrame
df.set_index("D", inplace=True)
print(df)
print("-------------------------------------")

#Print the name(s) of the index (now "D")
print(df.index.names)
print("-------------------------------------")

#Reset the index, moving the current index ("D") back to a regular column
df.reset_index(inplace=True)
print(df)
print("-------------------------------------")
