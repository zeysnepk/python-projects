import pandas as pd

#Specify the URL containing the HTML table
url = "https://www.contextures.com/xlsampledata01.html"

#Read the HTML table(s) from the URL into a list of DataFrames
dataset = pd.read_html(url, header=0)
print(dataset)
print("-----------------------------------------------------------")

#Print the number of tables found on the webpage
print(len(dataset))
print("-----------------------------------------------------------")

#Print the third table (index 2) from the list of DataFrames
print(dataset[2])