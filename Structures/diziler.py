ogrenciler = ["Zeynep","Yagmur","Saliha"]
print(ogrenciler)

#append --> diziye kararkter ekleme
ogrenciler.append("Ahmet")
print(ogrenciler)

#remove --> diziden karakter silme
ogrenciler.remove("Zeynep")
print(ogrenciler)

#dizileri listeleme
sehirler = list(("Ankara","Istanbul"))
print(sehirler)
print(len(sehirler)) 

#diziyi silme
print(sehirler.clear())
print(sehirler)

#dizideki karakter sayisi
sehirler = ["Ankara","Ankara","Istanbul"]
print("Ankara sayisi = " + str(sehirler.count("Ankara")))

#dizideli karakterin yeri
print("Istanbul indexi = " + str(sehirler.index("Istanbul")))

#dizideki index elemanini cikar
sehirler.pop(1)
print(sehirler)

#dizideki indexe eleman ekle
sehirler.insert(0,"Izmir")
print(sehirler)

#diziyi terse cevirme
sehirler.reverse()
print(sehirler)

#dizi referansi --> diziler pointer seklinde davranir direkt adrese gider
sehirler2 = sehirler
sehirler2[0] = "Yalova"
print(sehirler)

#dizi kopyalama
sehirler3 = sehirler.copy()
sehirler4 = sehirler
sehirler4[0] = "Kocaeli"
print(sehirler)
print(sehirler3)

#extend --> sehirleri birlestir
sehirler.extend(sehirler3)
print(sehirler)

#sort --> siralar
sehirler.sort()
print(sehirler)

sehirler.reverse()
print(sehirler)

#list in list
list = [[1,2],[3,7],[4,6,7]]
print(list[1])
print(list[1][1])
