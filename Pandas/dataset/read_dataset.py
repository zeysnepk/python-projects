import pandas as pd

#Load the dataset from a CSV file
csv_filename = "genshin_characters_v1.csv"
dataset = pd.read_csv(csv_filename)
print(dataset)
print("-----------------------------------------------------------------------")

#Drop the columns "arkhe" and "vision" from the dataset
new_dataset = dataset.drop(["arkhe", "vision"], axis=1)
print(new_dataset)

#Save the modified dataset to a new CSV file
new_dataset.to_csv("genshin_new.csv", index=False)

#Save the modified dataset to a new Excel file
new_dataset.to_excel("genshin_new.xlsx", index=False)