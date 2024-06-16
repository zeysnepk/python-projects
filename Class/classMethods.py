
class PersonINFO():
    
    def __init__(self, name, compNo, salary, languages):
        self.name = name
        self.compNo = compNo
        self.salary = salary
        self.languages = languages
        
    def printINFO(self):
        
        print(
        """
        
        PERSONAL INFORMATION:
        
        Name : {}
        
        Company No : {}
        
        Salary : {}
        
        Languages : {}  
              
        """.format(self.name, self.compNo, self.salary, self.languages))
        
    def increaseSalary(self, amount):
        
        self.salary += amount
        
    def addNewLanguage(self, NewLang):
        
        self.languages.append(NewLang)
        
        
Person1 = PersonINFO("Ahmet", "79843", 45000.50, ["Turkish", "English"])

Person1.printINFO()

Person1.increaseSalary(2500)
Person1.printINFO()

Person1.addNewLanguage("German")
Person1.printINFO()