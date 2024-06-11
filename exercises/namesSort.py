"""
Have 2 lists in your hand. Combine the first and last names from these lists and try to print the first and last names on the screen in order by *names*.

        name -----> [“Kerim”,“Tarık”,“Ezgi”,“Kemal”,“İlkay”,“Şükran”,“Merve”]

        last name ------> [“Yılmaz”, “Öztürk”, “Dağdeviren”, “Atatürk”, “Dikmen”, “Kaya”, “Polat”]

"""

names = ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]
lastNames = ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]

namesANDsurnames = list(zip(names,lastNames))

namesANDsurnames.sort()

for i, j in namesANDsurnames:
    print(i,j)