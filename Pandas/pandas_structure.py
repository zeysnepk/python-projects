import numpy as np
import pandas as pd

# Create a list of letters and numbers
letters = ["A", "B", "C", "D", "E", "F", "G"]
numbers = [1, 2, 3, 4, 5, 6, 7]

# Create a Pandas Series with letters as data and numbers as the index
letters_and_numbers = pd.Series(data=letters, index=numbers)
print(letters_and_numbers)

# Create a simple Pandas Series from a list of letters
print(pd.Series(letters))

# Create a NumPy array and convert it to a Pandas Series
npArray = np.array([10, 20, 30, 40, 50])
print(pd.Series(npArray)) 

# Create a Pandas Series from a dictionary
dictionary = {"A": 10, "B": 20, "C": 30, "D": 40, "E": 50}
print(pd.Series(dictionary))

# Create two dictionaries and convert them to Pandas Series
dict_1 = {"Blue": 12, "Green": 35, "Yellow": 1, "Pink": 7}
dict_1 = pd.Series(dict_1)
dict_2 = {"Orange": 5, "Yellow": 22, "Blue": 61, "Green": 23}
dict_2 = pd.Series(dict_2)

# Add the two Series together, aligning by index (key) and adding values
total_dict = dict_1 + dict_2
print(total_dict)

#Access specific elements in the Series using their index (key)
print(total_dict["Yellow"])
print(total_dict["Pink"])

#Get the keys (index) of the Series
print(total_dict.keys())

#Create a DataFrame from a dictionary with a single column "Serie"
serie = pd.DataFrame({'Serie': [1, 2, 3]})
print(serie)

#Create a range of dates starting from 2024-09-01 for 7 periods
dates = pd.date_range("20240901", periods=7)
print(dates)

#Create a DataFrame with random numbers, indexed by the first 4 dates and with npArray as column names
df = pd.DataFrame(np.random.randn(len(dates[:4]), len(npArray)), index=dates[:4], columns=npArray)
print(df)

#Create a DataFrame with various types of data, including dates, numbers, strings, and categorical data
df_2 = pd.DataFrame(
    {
        "Date": pd.Timestamp("20240901"),
        "Value": np.random.randn(5),
        "Name": np.array(["Alice", "Bob", "Charlie", "David", "Eve"]),
        "No": pd.Series(1, index=list(range(5)), dtype="float32"),
        "Group": pd.Categorical(["Group1", "Group2", "Group3", "Group4", "Group5"])
    }
)
print(df_2)
print("------------------------------------------------")

#Display the results based on specified Column
print(df_2["Name"])
print("------------------------------------------------")

#Display the results based on specified Row
print(df_2.loc[4]) #same with df_2.iloc[4]
print("------------------------------------------------")

#Display the results based on specified Columns
print(df_2[["Name", "Value"]])
print("------------------------------------------------")

#Adding a new column
df_2["Age"] = pd.Series([18, 36, 21, 49, 60], dtype=int)
print(df_2)
print("------------------------------------------------")

#Removing a column (if changes are to be implemented in dataFrame , inplace should be True!)
df_2.drop("No", axis=1, inplace=True)
print(df_2)
print("------------------------------------------------")

#Accessing specified columns or rows
print(df_2.loc[3, "Name"])
print("------------------------------------------------")

print(df_2.iloc[[2, 3], [2, 4]])
print("------------------------------------------------")

#Display the first 3 rows of the DataFrame
print(df_2.head(3))
print("------------------------------------------------")

#Display the last 2 rows of the DataFrame
print(df_2.tail(2))
print("------------------------------------------------")

#Display the index (row labels) of the DataFrame
print(df_2.index)
print("------------------------------------------------")

#Display the columns (column labels) of the DataFrame
print(df_2.columns)
print("------------------------------------------------")

#Display the data types of each column in the DataFrame
print(df_2.dtypes)
print("------------------------------------------------")

#Display a summary of the DataFrame's statistics
print(df_2.describe())
print("------------------------------------------------")

#Sort the DataFrame by columns in descending order
print(df_2.sort_index(axis=1, ascending=False))
print("------------------------------------------------")

#Sort the DataFrame by rows in descending order
print(df_2.sort_index(axis=0, ascending=False))
print("------------------------------------------------")

#Sort the DataFrame by the "Value" column in ascending order
print(df_2.sort_values(by="Value"))
print("------------------------------------------------")

