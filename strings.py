#upper() and lower() Functions
print("ZEYNEP".lower())
print("ZeyNep".lower())
print("zeynep".upper())
print("ZeYNeP".upper())

#replace() Function
print("My name is Zeynep".replace("e","i"))
print("My name is Zeynep".replace(" ","-"))
print("My name is Zeynep".replace("Zeynep","Nobody"))

#startswith() and endswith() Functions
print("Python".startswith("P"))
print("Python".startswith("py"))
print("Python".endswith("on"))
print("Python".endswith("an"))

#split() Function
listWords = "My name is Zeynep".split(" ")
print(listWords)

#strip() / lstrip() / rstrip() Functions
print("          python          ".strip() + ".")
print("          python          ".lstrip() + ".")
print("          python          ".rstrip() + ".")
print("<<<<<<<<<<<<<python>>>>>>>>>>>".strip(">") + ".")

#join() Function
listN = ["26","09","1882"]
print("/".join(listN))

listZ = ["T","B","M","M"]
print(".".join(listZ))

#count() Function
print("My name is Zeynep".count("e"))
print("My name is Zeynep".count(" "))
print("My name is Zeynep".count(" ",10)) #counts starting from 10th value

#find() and rfind() Functions
print("butterfly".find("t"))  #starts to find at the beginning
print("butterfly".find("c"))  #returns -1 if not found
print("butterfly".rfind("t")) #starts to find at the end
print("butterfly".rfind("a"))

