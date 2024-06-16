#Learn the values of the dollar, euro, gold and stock market instantly from https://www.doviz.com/ and try to develop a project using them.

#*Note: Develop this project using requests and beautifulsoup.

import requests
from bs4 import BeautifulSoup

url = "https://www.doviz.com/"

response = requests.get(url)

content = response.content
print(content)

soup = BeautifulSoup(content,"html.parser")
print(soup)

for i,j in zip(soup.find_all("span",{"class" : "name"}), soup.find_all("span", {"class" : "value"})):
    print("{} = {}".format(i.text,j.text))
    

