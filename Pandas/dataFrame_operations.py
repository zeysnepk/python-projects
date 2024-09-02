import numpy as np
import pandas as pd

#Creating a DataFrame with columns "No", "Grade", and "Name"
df = pd.DataFrame({
    "No": [1, 2, 3, 4, 5, 6],
    "Grade": [100, 70, 75, 100, 90, 75],
    "Name": ["John", "Alice", "Bob", "Charlie", "David", "Eve"]
})

print(df)
print("---------------------------------------------")

#Display the first 4 rows of the DataFrame
print(df.head(4))
print("---------------------------------------------")

#Display unique values in the "Grade" column
print(df["Grade"].unique())
print("---------------------------------------------")

#Display the number of unique values in the "Grade" column
print(df["Grade"].nunique())
print("---------------------------------------------")

#Count the frequency of each unique value in the "Grade" column
print(df["Grade"].value_counts())
print("---------------------------------------------")

#Filter rows where "Grade" is greater than or equal to 80 and the length of "Name" is less than 5 characters
print(df[(df["Grade"] >= 80) & (df["Name"].str.len() < 5)])
print("---------------------------------------------")

#Multiply each value in the "No" column by 3
df["No"] = df["No"].apply(lambda x: x*3)
print(df)
print("---------------------------------------------")

#Apply the `len` function to the "Name" column to get the length of each name
print(df["Name"].apply(len))
print("---------------------------------------------")

#Print the column names of the DataFrame
print(df.columns)
#Print the number of columns in the DataFrame
print(len(df.columns))
#Print the index (row labels) of the DataFrame
print(df.index)
#Print the number of rows in the DataFrame
print(len(df.index))
print("---------------------------------------------")

#Sort the DataFrame by the "Grade" column in descending order
print(df.sort_values("Grade", ascending=False))
print("---------------------------------------------")

#Create a new DataFrame with columns "Month", "City", and "Temperature"
df2 = pd.DataFrame({
    "Month": np.tile(["April", "December", "January"], 3),
    "City": np.repeat(["İstanbul", "Tokyo", "London"], 3),
    "Temperature": [8, 38, 32, 27, 16, 30, 5, 12, 9]
})

print(df2)
print("---------------------------------------------")

#Create a pivot table with "City" as the index, "Month" as columns, and "Temperature" as values
pivot_table = df2.pivot_table(index="City", columns="Month", values="Temperature")
print(pivot_table)