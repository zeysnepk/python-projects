
#tuple sadece okunur degistirilemez perfonmas icin ideal
tupleListe = (2,4,6,"hello",(1,2,3))
liste = [2,4,6,"hello",[1,2,3]]

liste[0] = 6  #bunu tuple ile yazamayiz hata verir

print(tupleListe)
print(liste)

print(type(tupleListe))
print(type(liste))

print(len(tupleListe))
print(len(liste))

print(tupleListe[-2])
print(liste[-2])

#2 dahil degil
print(tupleListe[1:2]) #burda virgulle ayirir 
print(liste[1:2])

#tek elemanda tuple asagidaki gibi farkli calisir
tupleOne = ("Zeynep")
print(tupleOne)
print(type(tupleOne)) #burda tipi str olarak gosterilir bunu duzeltmek icin virgul eklenmeli

tupleTwo = ("Zey",)
print(tupleTwo)
print(type(tupleTwo))

#count fonk
nums = (1,1,1,2,3,3,3,4)
print(nums.count(1))
