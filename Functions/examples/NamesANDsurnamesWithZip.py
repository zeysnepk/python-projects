"""
You have two lists of first and last names.

        isimler -----> [“Kerim”,“Tarık”,“Ezgi”,“Kemal”,“İlkay”,“Şükran”,“Merve”]

        surnames -----> [“Yılmaz”, “Öztürk”, “Dağdeviren”, “Atatürk”, “Dikmen”, “Kaya”, “Polat”]

Match these names and surnames in order and print them one after the other on the screen.
"""

names = ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]
surnames = ["Yılmaz", "Öztürk", "Dağdeviren", "Atatürk", "Dikmen", "Kaya", "Polat"]

namesANDsurnames = list(zip(names,surnames))

for i ,j in namesANDsurnames:
    print(i,j)