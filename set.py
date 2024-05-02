#setler daha hizli, elemanlar degistirilemez ve sirali degildir

cities = {"Istabul","Ankara","Kocaeli"}
print(cities) #belirli siralanisi yoktur cikti girdi gibi degil

for city in cities:
    print(city)

print("istanbul" in cities) #kucuk harfe duyarli false dondurur

if("Ankara" in cities):
    print("Listede var")

else:
    print("Listede yok")

cities.add("Izmir")
print(cities) #eleman eklenebilir random siraya girer

cities.update(["Yalova","Mersin"])  #birden fazla eleman icin kullanilabilir
print(cities)

print(len((cities)))

cities.remove("Izmir") #elemani siler
print(len(cities))

cities.discard("Adana") #remove kullanirken silincek eleman bulunmazsa hata verir, hata vermemesi icin discard kullanilabilir

x = cities.pop() #random elemani siler 
print(len(cities))
print(cities)

cities.clear() #tum elemanlari siler output-->set()
print(cities) 

cities2 = {"Istabul","Ankara","Kocaeli"}
del cities2 #set() output u gorunmemesi icin

#set union --> birlesim
setA = {1,2,3,4,5}
setB = {1,3,4,6,7,9}

print(setA | setB)
print(setA.union(setB))
print(setB.union(setA))

#set intersection --> kesisim
print(setA & setB)
print(setA.intersection(setB))
print(setB.intersection(setA))

#set difference --> fark
print(setA - setB)
print(setB - setA)
print(setA.difference(setB))
print(setB.difference(setA))

#set symmetric_difference --> simetrik fark
print(setA ^ setB)
print(setA.symmetric_difference(setB))
print(setB.symmetric_difference(setA))

#set dictionary
#set gibi sirasiz veri tutar
engtr = {"book" : "kitap","table" : "masa"}
print(engtr)

print(engtr["book"]) #sozlukteki degerini verir

engtr["pencil"] = "kalem"
print(engtr)

treng = dict(kitap = "book", masa = "table") #su sekilde de kullanilabilir
print(treng)

del(engtr["book"]) #o veriyi siler
print(engtr)

print(len(engtr))

#2-dimen
dicA = {"a1" : [1,2,3,4], "a2" : [[0,1],[3,4]]}
print(dicA["a1"])
print(dicA["a1"][1])
print(dicA["a2"][0])
print(dicA["a2"][0][1])

#keys and values of set dictionary
dicB = {"one" : 1, "two" : 2, "three" : 3}
print(dicB.keys())
print(dicB.values())
print(dicB.items())

for i,j in dicB.items():
    print(i,j)