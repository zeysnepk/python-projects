#takes common features from class to class
class Student():
    
    def __init__(self, name, age, school):
        
        self.name = name
        self.age = age
        self.school = school
        
    def printINFO(self):
        
        print("\nSTUDENT INFORMATION\n\nName : {}\nAge : {}\nSchool : {}\n\n".format(self.name, self.age, self.school))
        

class Teacher(Student):
    
    def __init__(self, name, age, school, salary):
        
        super().__init__(name,age,school) #super function takes common parametres in the class within this class
        
        self.salary = salary
    
    def printINFO(self):
        
        print("\nTEACHER INFORMATION\n\nName : {}\nAge : {}\nSchool : {}\nSalary : {}\n\n".format(self.name, self.age, self.school, self.salary))
    
    def IncreaseSalary(self, amount):
        
        self.salary += amount

student1 = Student("Zey", 19, "Kocaeli University")
student1.printINFO()

teacher1 = Teacher("Anf", 34, "Istanbul University",25000)
teacher1.printINFO()

teacher1.IncreaseSalary(2500)
teacher1.printINFO()

