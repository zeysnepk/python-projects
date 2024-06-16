
class student():
    
    name = "Zeynep"
    no = 20002020
    date = "11/09/2004"
    score = 2.12
    
    
student1 = student

print(student1)
print(student1.name)
print(student1.no)
print(student1.date)
print(student1.score)

print(student.name) #same with student1

#__INIT__ function
class Student():
    
    def __init__(self,name,no,date,score): #self is always writen to indicate student class
        self.name = name
        self.no = no
        self.date = date
        self.score = score
        
student2 = Student("Akfoj",8829292,"21/08/2001",3.12)
student3 = Student("Zoder",2889023,"07/12/2000",1.98)

print(student2.name)
print(student3.date)

#default values
class StudentDefault():
    
    def __init__(self,name = "NO INFO",no = "NO INFO",date = "NO INFO",score = 0):
        self.name = name
        self.no = no
        self.date = date
        self.score = score
        
student4 = StudentDefault(name = "Azel")

print(student4.name)
print(student4.no)
print(student4.score)


