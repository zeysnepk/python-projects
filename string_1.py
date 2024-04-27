
firstString = "zeynep kaplan"
secondString = "ZEYNEP Kaplan"

if (firstString.upper() == secondString.upper()):
    print("The string are same.")
else:
    print("The string are not same.")
    
#len
message = "Hello World"

for i in range(len(message)):
    print(message[i])

#substring
print("\n"+message[2:5])

print("\n"+message[2:]+"\n")

print(len(message))

print("\n"+message[0:len(message)])

#lower upper
print(message.upper())
print(message.lower())

#replace --> istenilen karakteri baska bir karakterle degistirir
string = "Merhaba dünya"
print(string.replace("ü","u")) #mesaj = string.replace("ü","u")

#split --> istenilen karaktere gore dizi seklinde ayirir
bilgi = "Zeynep Kaplan 19 Kocaeli"
print(bilgi.split())
print(bilgi.split("K"))
print("Adi = " + bilgi.split()[0])

#strip --> bastaki ve sondaki bosluklari atar
bilgi2 = "     Merhaba Ben Zey  "
bilgi3 = "     Merhaba Ben Zey  ".strip()
print(bilgi2.split(" "))
print(bilgi3.split(" "))

#input
ad = input("Adiniz? ")
print(ad)

ilkSayi = input("Ilk Sayi: ")
ikinciSayi = input("Ikinci Sayi: ")

print(ilkSayi + ikinciSayi) # --> İnputlari metinsel aldigi icin yanyana basar stringler gibi
print(int(ilkSayi) + int(ikinciSayi))

