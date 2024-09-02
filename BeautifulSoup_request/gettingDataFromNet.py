#Getting data with requests and BeautifulSoup from a website
import requests
from bs4 import BeautifulSoup

url = "https://github.com/zeysnepk"
response = requests.get(url) #passing url adress to response object

print(response)

content = response.content #getting content of address
print(content)
print("\n\n")

soup = BeautifulSoup(content, "html.parser") #passing content by parselling

print(soup)
print("\n\n")

print(soup.prettify()) #making content in a smoother looking shape

print(soup.find_all("a")) #printing data labeled "a" in a for loop

#printing data containing "href" in labeled "a"
for i in soup.find_all("a"):  
    print(i.get("href")) 
    print("**************************")
    
print("\n\n")

#printing data texts in labeled "a"
for i in soup.find_all("a"):
    print(i.text)
    print("**************************")
    

print(soup.find_all("div", {"class" : "Box d-flex p-3 width-full public source"}))

