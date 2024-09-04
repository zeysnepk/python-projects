import pandas as pd

filename = "input/Online_game.csv"

# Load the dataset from the CSV file
df = pd.read_csv(filename, index_col="Rank")
print(df)
print("-----------------------------------------------------------")

# Display the first 10 rows of the dataset
print(df.head(10))
print("-----------------------------------------------------------")

# Print the total number of rows in the dataset
print(len(df.index))
print("-----------------------------------------------------------")

# Calculate and print the mean of North American sales
print(df["NA_Sales"].mean())
print("-----------------------------------------------------------")

# Find and print the maximum North American sales
print(df["NA_Sales"].max())
print("-----------------------------------------------------------")

# Find and print the name of the oldest game in the dataset
print(df[df["Year"].min() == df["Year"]]["Name"].iloc[0])
print("-----------------------------------------------------------")

# Print the genre of the game "Minecraft"
print(df[df["Name"] == "Minecraft"]["Genre"].iloc[0])
print("-----------------------------------------------------------")

# Calculate and print the mean European sales for each platform
print(df.groupby("Platform")["EU_Sales"].mean())
print("-----------------------------------------------------------")

# Print the number of unique publishers in the dataset
print(df["Publisher"].nunique())
print("-----------------------------------------------------------")

# Print the count of games for each publisher
print(df["Publisher"].value_counts())
print("-----------------------------------------------------------")

# Find and print games with "ze" in their name (case-insensitive)
print(df[df["Name"].apply(lambda x: "ze" in x.lower())])

print("-----------------------------------------------------------")

# Find the game with the highest Global_Sales
print("Game with highest Global Sales:")
print(df.loc[df["Global_Sales"].idxmax()]["Name"])
print("-----------------------------------------------------------")

# Calculate the average Global_Sales for each Genre
print("Average Global Sales by Genre:")
print(df.groupby("Genre")["Global_Sales"].mean().sort_values(ascending=False))
print("-----------------------------------------------------------")

# Find the top 5 publishers by total Global_Sales
print("Top 5 Publishers by Total Global Sales:")
print(df.groupby("Publisher")["Global_Sales"].sum().sort_values(ascending=False).head())
print("-----------------------------------------------------------")

# Count the number of games released each year
print("Number of games released each year:")
print(df["Year"].value_counts().sort_index())
print("-----------------------------------------------------------")

# Find the game with the highest JP_Sales in each Genre
print("Game with highest JP Sales in each Genre:")
print(df.loc[df.groupby("Genre")["JP_Sales"].idxmax()][["Genre", "Name", "JP_Sales"]])
print("-----------------------------------------------------------")

# Calculate the correlation between different sales regions
print("Correlation between sales regions:")
print(df[["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales", "Global_Sales"]].corr())
print("-----------------------------------------------------------")

# Find games that have sold more in Europe than in North America
print("Games that sold more in Europe than in North America:")
print(df[df["EU_Sales"] > df["NA_Sales"]][["Name", "EU_Sales", "NA_Sales"]])
print("-----------------------------------------------------------")

# Calculate the percentage of total sales for each region
df["NA_Percentage"] = df["NA_Sales"] / df["Global_Sales"] * 100
df["EU_Percentage"] = df["EU_Sales"] / df["Global_Sales"] * 100
df["JP_Percentage"] = df["JP_Sales"] / df["Global_Sales"] * 100
df["Other_Percentage"] = df["Other_Sales"] / df["Global_Sales"] * 100

# Print the average percentage of sales by region
print("Average percentage of sales by region:")
print(df[["NA_Percentage", "EU_Percentage", "JP_Percentage", "Other_Percentage"]].mean())
print("-----------------------------------------------------------")

# Find the most common word in game titles (excluding common English words)
from collections import Counter
import re

def get_words(name):
    return re.findall(r'\w+', name.lower())

# Extract all words from game titles
all_words = [word for name in df["Name"] for word in get_words(name)]
word_counts = Counter(all_words)

# Define a set of common English words to exclude
common_words = set(['the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by'])
most_common_words = [word for word, count in word_counts.most_common() if word not in common_words]

# Print the 10 most common words in game titles
print("Most common words in game titles (excluding common English words):")
print(most_common_words[:10])
print("-----------------------------------------------------------")
