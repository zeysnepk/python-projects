import numpy as np
import pandas as pd

#Create a NumPy array with some NaN values
arr = np.array([[10, 20, np.nan], [5, np.nan, np.nan], [21, np.nan, 10]])
print(arr)

#Convert the NumPy array into a DataFrame with specified row and column labels
df = pd.DataFrame(arr, ["Row1", "Row2", "Row3"], ["Column1", "Column2", "Column3"])
print(df)
print("------------------------------------------------")

#Drop rows that contain any NaN values
print(df.dropna())
print("------------------------------------------------")

#Drop columns that contain any NaN values
print(df.dropna(axis=1))
print("------------------------------------------------")

#Drop rows that have less than 2 non-NaN values
print(df.dropna(thresh=2))
print("------------------------------------------------")

#Fill all NaN values with 1
print(df.fillna(value=1))
print("------------------------------------------------")

#Calculate the sum of all values in the DataFrame
sum_data = df.sum().sum()
#Fill all NaN values with the sum of all values
print(df.fillna(value=sum_data))
print("------------------------------------------------")

#Count the total number of NaN and non-NaN values
null_count = df.isnull().sum().sum()
notnull_count = df.notnull().sum().sum()

#Calculate the mean of all non-NaN values
mean = sum_data / notnull_count
print(mean)

#Fill NaN values in the DataFrame with the calculated mean and update the DataFrame in place
df.fillna(value=mean, inplace=True)
print(df)
print("------------------------------------------------")

#Create a series of consecutive days starting from a specific date
start_date = pd.Period("2025-01-01", freq='D')
#Generate the date series and reindex to include an extra index (4), which will create a NaN value
date_data = pd.Series([start_date + i for i in range(4)]).reindex([0, 1, 2, 3, 4])
print(date_data)