#Writing an exchange program that converts first currency to second currency using Requests Module and json, for this data must be received from frankfurter.app as a json object 

import requests

url = "https://www.frankfurter.app/latest?base="

first_currency = input("First Currency : ")
second_currency = input("Second Currency : ")
amount = float(input("Amount : "))

response = requests.get(url + first_currency)

print(response)

jsonData = response.json()
print(jsonData)

print("\n\n")

print(jsonData["rates"][second_currency])

result = amount * jsonData["rates"][second_currency]

print("\n\n")

print(amount, first_currency, "is", result, second_currency, ".")

