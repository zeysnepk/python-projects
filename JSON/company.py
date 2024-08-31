import json

with open('company.json', 'r') as file:
    def read_company_info():
        data = json.load(file)
        print("Company Name:", data["company"]["name"])
        print("Founded Year:", data["company"]["establishedYear"])
        print("Employees")
        print("********************************")
        for employee in data["company"]["employees"]:
            print("ID:", employee["id"])
            print("Name:", employee["firstName"])
            print("Surname:", employee["lastName"])
            print("Position:", employee["position"])
            print("-------------------------------------------")
        print("Clients")
        print("********************************")
        for client in data["company"]["clients"]:
            print("ID:", client["id"])
            print("Name:", client["name"])
            print("Company:", client["company"])
            print("Email:", client["email"])
            print("-------------------------------------------")
        print("Warehouses")
        print("********************************")
        for warehouse in data["company"]["warehouses"]:
            print("ID:", warehouse["id"])
            print("Location:", warehouse["location"])
            print("Capasity:", warehouse["capacity"])
            print("Stock:", warehouse["stock"])
            print("-------------------------------------------")
        print()
        print()
            
            
    read_company_info()
    print("*********************************************")
    
    
    
    
    
