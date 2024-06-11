"""
Create a file called “poem.txt” and include the following lines.

                    Memlekete sis çökmüş bir gece 
                    Usulca yanağıma sen düşüyorsun
                    Sabah saat dokuzu beş geçe
                    Terk edip bizleri gidiyorsun
                    Ayrılık bu kadar yakmamıştı içimizi
                    Farkında mısın bilmiyorum
                    Aldın beraberinde cumhuriyetimizi
                    Korkunç bir veda, sararmıştı her yer
                    Ellerini uzat tutmak istiyoruz
                    Masmavi gözleri kaybetmiş çocuk
                    Aldı bir sabah ruhumuzu
                    Lakin nasıl bölmesin yokluğun uykumuzu

Read each line of this file. Add the initials of the lines together to form a string and print this string on the screen.
"""
firstLetters = []

with open ("poem.txt","r") as poem:
    
    for i in poem:
        firstLetters.append(i[0])
        
print("".join(firstLetters))