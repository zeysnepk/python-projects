import sqlite3

con = sqlite3.connect("lib.db")
cursor = con.cursor()




con.close()