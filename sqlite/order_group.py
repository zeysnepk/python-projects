import sqlite3

con = sqlite3.connect("lib.db")
cursor = con.cursor()


def order_names():
    ordered = cursor.execute("SELECT Name FROM firstable ORDER BY Name").fetchall()
    
    for name in ordered:
        print(name)
        
def author_or_publisher():
    ordered = cursor.execute("SELECT Name FROM firstable WHERE author='Dostoyevski' or publisher='Michael Joseph' ORDER BY Author desc").fetchall() #default is asc

    for name in ordered:
        print(name)
        
order_names()
print("----------------------------------")
author_or_publisher()
print("----------------------------------")

def group_by_publisher():
    grouped = cursor.execute("SELECT Publisher, COUNT(*) FROM firstable GROUP BY Publisher ORDER BY COUNT(*) desc").fetchall()

    for row in grouped:
        print("Publisher:", row[0], "| Number:", row[1])
        

def group_by_author_count():
    grouped = cursor.execute("SELECT Author, COUNT(*) FROM firstable GROUP BY Author HAVING COUNT(*) > 4").fetchall()

    for row in grouped:
        print("Author:", row[0], "| Number:", row[1])
        
        
group_by_publisher()
print("----------------------------------")
group_by_author_count()

con.close()