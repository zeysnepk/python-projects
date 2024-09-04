import pandas as pd

#Load the Netflix dataset
filename = "input/netflix_titles.csv"    
df = pd.read_csv(filename, index_col="show_id")

#Drop the 'description' column as it is not needed for the analysis
df.drop("description", axis=1, inplace=True)

#Display the first 5 rows of the DataFrame
df.head(5)

#Get the number of rows in the DataFrame
len(df.index)

#Get the number of columns in the DataFrame
len(df.columns)

#Calculate the mean release year of all titles
df["release_year"].mean()

#Find the title of the most recent movie
df[(df["release_year"] == df["release_year"].max()) & (df["type"] == "Movie")].iloc[0]["title"]

#Find the title of the oldest TV show
df[(df["release_year"] == df["release_year"].min()) & (df["type"] == "TV Show")].iloc[0]["title"]

#Group the DataFrame by 'type' (Movie or TV Show) and calculate the mean release year for each group
group_type = df.groupby("type")
group_type[["release_year"]].mean()

#Count the number of occurrences of each 'type'
df["type"].value_counts()

#Calculate the length of each title (excluding spaces) and add it as a new column 'title_length'
df["title_length"] = df["title"].str.replace(" ","").str.len()

#Count the number of genres listed in the 'listed_in' column and add it as a new column 'genres_count'
df["genres_count"] = df["listed_in"].apply(lambda x: len(x.split(",")))

#Calculate the 'score' as the ratio of 'title_length' to the sum of 'title_length' and 'genres_count'
total = df["title_length"] + df["genres_count"]
df["score"] = df["title_length"] / total

#Sort the DataFrame by 'score' in descending order
df.sort_values("score", ascending=False)

#Swap the contents of the 'type' and 'title' columns
df["type"], df["title"] = df["title"], df["type"]

#Swap the contents of the 'type' and 'title' columns
df.rename(columns={"type": "title", "title": "type"}, inplace=True)

#Create a new DataFrame for movies only
movies_df = df[df["type"] == "Movie"]
movies_df.reset_index(inplace=True) #Reset the index
movies_df.drop("show_id",axis=1 ,inplace=True) #Drop the 'show_id' column
movies_df.to_csv("input/netflix_movies.csv", index=False) #Save to a new CSV file

#Create a new DataFrame for TV shows only
tvshows_df = df[df["type"] == "TV Show"]
tvshows_df.reset_index(inplace=True)
tvshows_df.drop("show_id",axis=1 ,inplace=True)
tvshows_df.to_csv("input/netflix_tvshows.csv", index=False)   




