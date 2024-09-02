#getting movies data from IMDb

import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}
response = requests.get(url, headers=headers)

content = response.content
soup = BeautifulSoup(content, "html.parser")


print(soup.prettify())
print("*******************************************")


for i in soup.find_all("h3", {"class", "ipc-title__text"}):
    if i.text == "Recently viewed":
        break
    print(i.text)

print("******************************************************\nRATES")

for i in soup.find_all("div", {"class", "sc-e2dbc1a3-0 ajrIH sc-b189961a-2 fkPBP cli-ratings-container"}):
    print(i.text)
    
    
moviesName = soup.find_all("h3", {"class", "ipc-title__text"})
moviesRate = soup.find_all("div", {"class", "sc-e2dbc1a3-0 ajrIH sc-b189961a-2 fkPBP cli-ratings-container"})

for i in range(0, len(moviesRate)):
    print(moviesName[i + 1].text, "----->", moviesRate[i].text)
    
#or

moviesName.pop(0)
print("\nMOVIES AND RATINGS")
for movieName, movieRate in zip(moviesName, moviesRate):
    
    movieName = movieName.text
    movieRate = movieRate.text.split("(")
    movieRate = movieRate[0].strip()
    
    print(movieName, "----->", movieRate)
   
#Printing movies whose rate is greater than the rate value received from the user 
try:
    rateNum = float(input("Enter rating: "))
    
    print("\nSUGGESTIONS")
    
    for movie_name, movie_rate in zip(moviesName, moviesRate):
    
        movie_name = movie_name.text
        movie_name = movie_name.split(".")
        movie_name = movie_name[1]
        movie_name = movie_name.strip(" ")
        movie_rate = movie_rate.text.split("(")
        movie_rate = movie_rate[0].strip()

        if float(movie_rate) >= rateNum:
            print(movie_name, "----->", movie_rate)
    
except ValueError:
    print("INVALID INPUT")
