class Student:  #class
    name="John" #class attribute
    section="3A"
    roll="16"
    marks="87" 

    def objprint(self):
        print("The name is",self.name)

Student.name="John N" #class attribute
john=Student() #Object
sam=Student()
print(john.section)

print(john.name)
print(sam.name)

sam.name="Sam" # instance attribute

print(sam.name)
print(john.name)