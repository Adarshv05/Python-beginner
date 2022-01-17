class Student:  #class
    name="John"
    section="3A"
    roll="16"
    marks="87"

    def objprint(self):
        print("The name is",self.name)

    @staticmethod 
    def gm():
        print("Cool")

john=Student() #Object
print(john.section)
print(john.name)

john.objprint() #calling self
Student.objprint(john) 

john.gm()
Student.gm()