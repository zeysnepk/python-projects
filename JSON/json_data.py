import json

data = '{"name" : "Zeynep", "age" : 19, "city" : "Istanbul"}' #a sample JSON string
converted_data = json.loads(data) #convert JSON string to Python dictionary

print(converted_data["name"])
print(converted_data["age"])
print(converted_data["city"])

data = {"name" : "Zeynep", "age" : 19, "city" : "Istanbul"} #a sample Python dictionary
converted_data = json.dumps(data) #convert Python dictionary to JSON string

print(converted_data)