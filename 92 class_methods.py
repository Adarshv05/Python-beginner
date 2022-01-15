class Student:  #class
    name="John"
    section="3A"
    roll="16"
    marks="87"

    def objprint(self):
        print("The name is",self.name)

john=Student() #Object
print(john.section)
print(john.name)

john.objprint()