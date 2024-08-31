import sqlite3

con = sqlite3.connect("lib.db")
cursor = con.cursor()

def name_include_a():
    data = cursor.execute("SELECT Name FROM firstable WHERE Name LIKE '%a%'").fetchall()

    for name in data:
        print(name[0])
        
def name_ended_u():
    data = cursor.execute("SELECT Name FROM firstable WHERE Name LIKE '%u'").fetchall()

    for name in data:
        print(name[0])
        
def name_started_m():
    data = cursor.execute("SELECT Name FROM firstable WHERE Name LIKE 'C%'").fetchall()

    for name in data:
        print(name[0])

def name_started_ad():
    data = cursor.execute("SELECT Name FROM firstable WHERE Name LIKE 'ad%'").fetchall()

    for name in data:
        print(name[0])

name_include_a()
print("----------------------------------")
name_ended_u()
print("----------------------------------")
name_started_m()
print("----------------------------------")
name_started_ad()
con.close()